from src.login_module import Login
from src.form_functionality import Form

class TestExamples:
    def test_001(self):
        form = Form()
        actual_message = form.enter_name('djagstrgebsassditsatasgsjabastsbdbasals')
        assert actual_message == 'Invalid value'
