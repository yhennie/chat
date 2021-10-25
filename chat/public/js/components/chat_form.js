import { create_guest } from './chat_utils';
import ChatSpace from './chat_space';

export default class ChatForm {
  constructor(opts) {
    this.$wrapper = opts.$wrapper;
    this.profile = opts.profile;
    this.setup();
  }

  setup() {
    this.$chat_form = $(document.createElement('div'));
    this.$chat_form.addClass('chat-form');
    this.setup_header();
    this.setup_form();
  }

  setup_header() {
    this.avatar_html = frappe.avatar(null, 'avatar-medium', this.profile.name);
    const header_html = `
			<div class='chat-header mb-2'>
				${this.avatar_html}
				<div class='chat-profile-info'>
					<div class='chat-profile-name'>
						${__(this.profile.name)}
						<div class='online-circle'></div>
					</div>
					<div class='chat-profile-status'>${__('Typically replies in a few hours')}</div>
				</div>
			</div>
		`;
    this.$chat_form.append(header_html);
  }

  setup_form() {
    const form_html = `
			<div class='chat-form-container'>
				<p class='chat-query-heading'>${__('Consistent Helpdesk Portal')}</p>
		 
			</div>
		`;
    const footer_html = `
      <a class='chat-footer' target='_blank' href=''>
        ${__('Consistent MIT')}
      </a>
    `;
    this.$chat_form.append(form_html + footer_html);
  }

  get_values() {
    const result = {
      email: $('#chat-email').val(),
      full_name: $('#chat-fullname').val(),
      message: $('#chat-message-area').val(),
    };
    return result;
  }

  async validate_form() {
    try {
      const form_values = this.get_values();
      const res = await create_guest(form_values);

      if (!res) {
        return;
      }
      const query_message = {
        content: form_values.message,
        creation: new Date(),
        sender: res.guest_name,
        sender_email: res.email,
      };
      localStorage.setItem('guest_token', res.token);

      let profile = {
        room_name: this.profile.name,
        room: res.room,
        is_admin: this.profile.is_admin,
        user: res.guest_name,
        user_email: res.email,
        message: query_message,
        room_type: res.room_type,
      };

      const chat_space = new ChatSpace({
        $wrapper: this.$wrapper,
        profile: profile,
      });
    } catch (error) {
      //pass
    }
  }

  render() {
    this.$wrapper.html(this.$chat_form);
    const me = this;
    $('#submit-form').on('click', function () {
      me.validate_form();
    });
  }
}
