var portal = {

    init: function() {
        portal.get_elements();
        portal.init_fields();
        portal.init_login();
    },

    get_elements: function() {
        portal.type_element = document.querySelector('#type');
        portal.field_elements = document.querySelectorAll('input')
        portal.username_element = document.querySelector('#username');
        portal.password_element = document.querySelector('#password');
        portal.login_element = document.querySelector('#login');
        portal.error_element = document.querySelector('#error');
    },

    init_fields: function() {
        portal.field_elements.forEach(function(element) {
            element.addEventListener('keydown', function(event) {
                element.style.border = '0px';
                portal.error_element.style.display = 'none';
            });
        });
    },

    init_login: function() {
        portal.field_elements.forEach(function(element) {
            element.addEventListener('keypress', function(event) {
                if (event.keyCode == 13) portal.login();
            });
        });
        portal.login_element.addEventListener('click', function() {
            portal.login();
        });
    },

    login: function() {
        if (!portal.login_element.classList.contains('w3-disabled')) {
            var type = portal.type_element.value;
            var username = portal.username_element.value;
            var password = portal.password_element.value;
            if (filled(username)) {
                if (filled(password)) {
                    var data = {
                        type: type,
                        username: username,
                        password: password
                    };
                    ajax(
                        'POST',
                        '/login', data,
                        portal.loading
                    );
                } else portal.password_element.style.border = 'solid 2px red';
            } else portal.username_element.style.border = 'solid 2px red';
        }
    },

    loading: function() {
        portal.login_element.classList.add('w3-disabled');
        var t = setTimeout(function() {
            portal.login_element.classList.remove('w3-disabled');
            portal.error_element.style.display = 'block';
        }, 2000);
    }

};


document.addEventListener('DOMContentLoaded', portal.init);
