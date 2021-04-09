import pytest
#import tftest
from azure.identity import AzureCliCredential
from azure.mgmt.resource import ResourceManagementClient
import os


def test_apply(run_apply):
    assert "Apply complete!" in run_apply
    print('Testing clean apply')


def test_output(run_output):
    credential = AzureCliCredential()
    subscription_id = 'c65eaf3d-141a-4b75-9642-61a4c76ae763'
    resource_client = ResourceManagementClient(credential, subscription_id)
    assert resource_client.resource_groups.get(
        'myResourceGroup').name == run_output['something']
    print('Testing clean apply')


def test_destroy(run_destroy, run_output):
    run_destroy
    assert list(run_output.keys()) == []
    print('Testing clean destroy')
