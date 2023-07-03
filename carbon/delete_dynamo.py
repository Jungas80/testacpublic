import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('american-chip-cloud-instances-compare')

items = [
"na1.4xlarge",
"na1.large",
"na1.medium",
"na1.metal",
"na1.xlarge",
"nc1.medium",
"nc1.xlarge",
"nc3.2xlarge",
"nc3.4xlarge",
"nc3.8xlarge",
"nc3.large",
"nc3.xlarge",
"nc4.2xlarge",
"nc4.4xlarge",
"nc4.8xlarge",
"nc4.large",
"nc4.xlarge",
"nc5.12xlarge",
"nc5.18xlarge",
"nc5.24xlarge",
"nc5.2xlarge",
"nc5.4xlarge",
"nc5.9xlarge",
"nc5.large",
"nc5.metal",
"nc5.xlarge",
"nc5a.12xlarge",
"nc5a.16xlarge",
"nc5a.24xlarge",
"nc5a.2xlarge",
"nc5a.4xlarge",
"nc5a.8xlarge",
"nc5a.large",
"nc5a.xlarge",
"nc5ad.12xlarge",
"nc5ad.16xlarge",
"nc5ad.24xlarge",
"nc5ad.2xlarge",
"nc5ad.4xlarge",
"nc5ad.8xlarge",
"nc5ad.large",
"nc5ad.xlarge",
"nc5d.12xlarge",
"nc5d.18xlarge",
"nc5d.24xlarge",
"nc5d.2xlarge",
"nc5d.4xlarge",
"nc5d.9xlarge",
"nc5d.large",
"nc5d.metal",
"nc5d.xlarge",
"nc5n.18xlarge",
"nc5n.2xlarge",
"nc5n.4xlarge",
"nc5n.9xlarge",
"nc5n.large",
"nc5n.metal",
"nc5n.xlarge",
"nc6g.12xlarge",
"nc6g.16xlarge",
"nc6g.2xlarge",
"nc6g.4xlarge",
"nc6g.8xlarge",
"nc6g.large",
"nc6g.medium",
"nc6g.metal",
"nc6g.xlarge",
"nc6gd.12xlarge",
"nc6gd.16xlarge",
"nc6gd.2xlarge",
"nc6gd.4xlarge",
"nc6gd.8xlarge",
"nc6gd.large",
"nc6gd.medium",
"nc6gd.metal",
"nc6gd.xlarge",
"nc6gn.12xlarge",
"nc6gn.16xlarge",
"nc6gn.2xlarge",
"nc6gn.4xlarge",
"nc6gn.8xlarge",
"nc6gn.large",
"nc6gn.medium",
"nc6gn.xlarge",
"ncc2.8xlarge",
"ncr1.8xlarge",
"nd2.2xlarge",
"nd2.4xlarge",
"nd2.8xlarge",
"nd2.xlarge",
"nd3.2xlarge",
"nd3.4xlarge",
"nd3.8xlarge",
"nd3.xlarge",
"nd3en.12xlarge",
"nd3en.2xlarge",
"nd3en.4xlarge",
"nd3en.6xlarge",
"nd3en.8xlarge",
"nd3en.xlarge",
"nf1.16xlarge",
"nf1.2xlarge",
"nf1.4xlarge",
"ng2.2xlarge",
"ng2.8xlarge",
"ng3.16xlarge",
"ng3.4xlarge",
"ng3.8xlarge",
"ng3s.xlarge",
"ng4ad.16xlarge",
"ng4ad.4xlarge",
"ng4ad.8xlarge",
"ng4dn.12xlarge",
"ng4dn.16xlarge",
"ng4dn.2xlarge",
"ng4dn.4xlarge",
"ng4dn.8xlarge",
"ng4dn.metal",
"ng4dn.xlarge",
"nh1.16xlarge",
"nh1.2xlarge",
"nh1.4xlarge",
"nh1.8xlarge",
"nhs1.8xlarge",
"ni2.2xlarge",
"ni2.4xlarge",
"ni2.8xlarge",
"ni2.xlarge",
"ni3.16xlarge",
"ni3.2xlarge",
"ni3.4xlarge",
"ni3.8xlarge",
"ni3.large",
"ni3.metal",
"ni3.xlarge",
"ni3en.12xlarge",
"ni3en.24xlarge",
"ni3en.2xlarge",
"ni3en.3xlarge",
"ni3en.6xlarge",
"ni3en.large",
"ni3en.metal",
"ni3en.xlarge",
"ninf1.24xlarge",
"ninf1.2xlarge",
"ninf1.6xlarge",
"ninf1.xlarge",
"nm1.large",
"nm1.medium",
"nm1.small",
"nm1.xlarge",
"nm2.2xlarge",
"nm2.4xlarge",
"nm2.xlarge",
"nm3.2xlarge",
"nm3.large",
"nm3.medium",
"nm3.xlarge",
"nm4.10xlarge",
"nm4.16xlarge",
"nm4.2xlarge",
"nm4.4xlarge",
"nm4.large",
"nm4.xlarge",
"nm5.12xlarge",
"nm5.16xlarge",
"nm5.24xlarge",
"nm5.2xlarge",
"nm5.4xlarge",
"nm5.8xlarge",
"nm5.large",
"nm5.metal",
"nm5.xlarge",
"nm5a.12xlarge",
"nm5a.16xlarge",
"nm5a.24xlarge",
"nm5a.2xlarge",
"nm5a.4xlarge",
"nm5a.8xlarge",
"nm5a.large",
"nm5a.xlarge",
"nm5ad.12xlarge",
"nm5ad.16xlarge",
"nm5ad.24xlarge",
"nm5ad.2xlarge",
"nm5ad.4xlarge",
"nm5ad.8xlarge",
"nm5ad.large",
"nm5ad.xlarge",
"nm5d.12xlarge",
"nm5d.16xlarge",
"nm5d.24xlarge",
"nm5d.2xlarge",
"nm5d.4xlarge",
"nm5d.8xlarge",
"nm5d.large",
"nm5d.metal",
"nm5d.xlarge",
"nm5dn.12xlarge",
"nm5dn.16xlarge",
"nm5dn.24xlarge",
"nm5dn.2xlarge",
"nm5dn.4xlarge",
"nm5dn.8xlarge",
"nm5dn.large",
"nm5dn.metal",
"nm5dn.xlarge",
"nm5n.12xlarge",
"nm5n.16xlarge",
"nm5n.24xlarge",
"nm5n.2xlarge",
"nm5n.4xlarge",
"nm5n.8xlarge",
"nm5n.large",
"nm5n.metal",
"nm5n.xlarge",
"nm5zn.12xlarge",
"nm5zn.2xlarge",
"nm5zn.3xlarge",
"nm5zn.6xlarge",
"nm5zn.large",
"nm5zn.metal",
"nm5zn.xlarge",
"nm6g.12xlarge",
"nm6g.16xlarge",
"nm6g.2xlarge",
"nm6g.4xlarge",
"nm6g.8xlarge",
"nm6g.large",
"nm6g.medium",
"nm6g.metal",
"nm6g.xlarge",
"nm6gd.12xlarge",
"nm6gd.16xlarge",
"nm6gd.2xlarge",
"nm6gd.4xlarge",
"nm6gd.8xlarge",
"nm6gd.large",
"nm6gd.medium",
"nm6gd.metal",
"nm6gd.xlarge",
"nm6i.12xlarge",
"nm6i.16xlarge",
"nm6i.24xlarge",
"nm6i.2xlarge",
"nm6i.32xlarge",
"nm6i.4xlarge",
"nm6i.8xlarge",
"nm6i.large",
"nm6i.xlarge",
"np2.16xlarge",
"np2.8xlarge",
"np2.xlarge",
"np3.16xlarge",
"np3.2xlarge",
"np3.8xlarge",
"np3dn.24xlarge",
"np4d.24xlarge",
"nr3.2xlarge",
"nr3.4xlarge",
"nr3.8xlarge",
"nr3.large",
"nr3.xlarge",
"nr4.16xlarge",
"nr4.2xlarge",
"nr4.4xlarge",
"nr4.8xlarge",
"nr4.large",
"nr4.xlarge",
"nr5.12xlarge",
"nr5.16xlarge",
"nr5.24xlarge",
"nr5.2xlarge",
"nr5.4xlarge",
"nr5.8xlarge",
"nr5.large",
"nr5.metal",
"nr5.xlarge",
"nr5a.12xlarge",
"nr5a.16xlarge",
"nr5a.24xlarge",
"nr5a.2xlarge",
"nr5a.4xlarge",
"nr5a.8xlarge",
"nr5a.large",
"nr5a.xlarge",
"nr5ad.12xlarge",
"nr5ad.16xlarge",
"nr5ad.24xlarge",
"nr5ad.2xlarge",
"nr5ad.4xlarge",
"nr5ad.8xlarge",
"nr5ad.large",
"nr5ad.xlarge",
"nr5b.12xlarge",
"nr5b.16xlarge",
"nr5b.24xlarge",
"nr5b.2xlarge",
"nr5b.4xlarge",
"nr5b.8xlarge",
"nr5b.large",
"nr5b.metal",
"nr5b.xlarge",
"nr5d.12xlarge",
"nr5d.16xlarge",
"nr5d.24xlarge",
"nr5d.2xlarge",
"nr5d.4xlarge",
"nr5d.8xlarge",
"nr5d.large",
"nr5d.metal",
"nr5d.xlarge",
"nr5dn.12xlarge",
"nr5dn.16xlarge",
"nr5dn.24xlarge",
"nr5dn.2xlarge",
"nr5dn.4xlarge",
"nr5dn.8xlarge",
"nr5dn.large",
"nr5dn.metal",
"nr5dn.xlarge",
"nr5n.12xlarge",
"nr5n.16xlarge",
"nr5n.24xlarge",
"nr5n.2xlarge",
"nr5n.4xlarge",
"nr5n.8xlarge",
"nr5n.large",
"nr5n.metal",
"nr5n.xlarge",
"nr6g.12xlarge",
"nr6g.16xlarge",
"nr6g.2xlarge",
"nr6g.4xlarge",
"nr6g.8xlarge",
"nr6g.large",
"nr6g.medium",
"nr6g.metal",
"nr6g.xlarge",
"nr6gd.12xlarge",
"nr6gd.16xlarge",
"nr6gd.2xlarge",
"nr6gd.4xlarge",
"nr6gd.8xlarge",
"nr6gd.large",
"nr6gd.medium",
"nr6gd.metal",
"nr6gd.xlarge",
"nt1.micro",
"nt2.2xlarge",
"nt2.large",
"nt2.medium",
"nt2.micro",
"nt2.nano",
"nt2.small",
"nt2.xlarge",
"nt3.2xlarge",
"nt3.large",
"nt3.medium",
"nt3.micro",
"nt3.nano",
"nt3.small",
"nt3.xlarge",
"nt3a.2xlarge",
"nt3a.large",
"nt3a.medium",
"nt3a.micro",
"nt3a.nano",
"nt3a.small",
"nt3a.xlarge",
"nt4g.2xlarge",
"nt4g.large",
"nt4g.medium",
"nt4g.micro",
"nt4g.nano",
"nt4g.small",
"nt4g.xlarge",
"nx1.16xlarge",
"nx1.32xlarge",
"nx1e.16xlarge",
"nx1e.2xlarge",
"nx1e.32xlarge",
"nx1e.4xlarge",
"nx1e.8xlarge",
"nx1e.xlarge",
"nx2gd.12xlarge",
"nx2gd.16xlarge",
"nx2gd.2xlarge",
"nx2gd.4xlarge",
"nx2gd.8xlarge",
"nx2gd.large",
"nx2gd.medium",
"nx2gd.metal",
"nx2gd.xlarge",
"nz1d.12xlarge",
"nz1d.2xlarge",
"nz1d.3xlarge",
"nz1d.6xlarge",
"nz1d.large",
"nz1d.metal",
"nz1d.xlarge",
]

for item in items:
    table.delete_item(
        Key={
            'cloud_provider_id': 'aws',
            'instance_id': item
        }
    )