var api_key = '9863023bA7320AA73d79d81Ace035fc9'


function connect_websocket() {
    if (window.location.protocol == 'http:') {
        web_socket = new WebSocket('ws://' + window.location.host + '/ws/');
    } else {
        web_socket = new WebSocket('wss://' + window.location.host + '/ws/');
    }
}

function check_websocket_state() {
    if (web_socket.readyState != 1) {
        web_socket.close();
        connect_websocket();
    }
}

function send_data(data) {
        try {
            web_socket.send(JSON.stringify(data));
        } catch (error) {
            check_websocket_state();
            setTimeout(500, send_data, data);
        }
    }

function get_numbers_status(){
    data = {
        'method': 'getNumbersStatus',
        'country': 0,
        'api_key': api_key
    };
    send_data(data);
}

function registerAccounts(){
    data = {
        'method': 'registerAccounts',
        'country': 0,
        'accounts_number': 1,
        'api_key': api_key,
    };
    send_data(data);
}


connect_websocket();


