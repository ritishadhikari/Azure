Configuration MyDscConfiguration
{
    param
    (
        [string[]]$ComputerName="Localhost"
    )
    Node $ComputerName
    {
        WindowsFeature MyFeatureInstance
        {
            Ensure="Present"
            Name="RSAT"
        }
        WindowsFeature My2ndFeatureInstance
        {
            Ensure="Present"
            Name="Bitlocker"
        }
    }
}

