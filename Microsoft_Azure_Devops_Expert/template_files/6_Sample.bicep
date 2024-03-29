@minLength(3)
@maxLength(11)
param storagePrefix string

param storageSKU string = 'Standard_LRS'
param location string = resourceGroup().location

var uniqueStorageName = '${storagePrefix}${uniqueString(resourceGroup().id)}'

resource storage 'Microsoft.Storage/storageAccounts@2021-02-01' ={
  name: uniqueStorageName
  location: location
  kind: storageSKU
  sku: {
    name: 'Standard_LRS'
  }
}

resource service 'Microsoft.Storage/storageAccounts/fileServices@2021-02-01' ={
  name: 'default'
  parent: storage
}

resource share 'Microsoft.Storage/storageAccounts/fileServices/shares@2021-02-01' ={
  name: 'exampleshare'
  parent: service
}

module webModule './6_Main.bicep' ={
  name: 'webDeploy'
  params:{
    location: location
    storageName: storageSKU
  }
}

output storageEndpoint object =storage.properties.primaryEndpoints
