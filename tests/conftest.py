import pytest
import tftest


@pytest.fixture
def run_apply():
    tf = tftest.TerraformTest('../')
    return tf.apply()


@pytest.fixture
def run_destroy():
    tf = tftest.TerraformTest('../')
    return tf.destroy()


@pytest.fixture
def run_output():
    tf = tftest.TerraformTest('../')
    return tf.output()
