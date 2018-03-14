#!/usr/bin/python
import boto3
import argparse

def copy_database(source_aws_profile, target_aws_profile, *databases):
    print("copying %s from '%s' to '%s'" % (databases, source_aws_profile, target_aws_profile))
    source = boto3.Session(profile_name=source_aws_profile)
    target = boto3.Session(profile_name=target_aws_profile)
    src_client, target_client = source.client('glue'), target.client('glue')
    for db in databases:
        print(target_client.create_database(DatabaseInput={'Name': db}))
        for table in src_client.get_tables(DatabaseName = db)['TableList']:
            table.pop('CreateTime')
            table.pop('LastAccessTime')
            print(target_client.create_table(DatabaseName = db, TableInput = table))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('databases', metavar = "<database-name>", nargs='+', help='Database list that needs copying')
    parser.add_argument('--from', dest = 'src', metavar = '<aws-profile>', help='profile name for aws account from which to copy (use "aws configure --profile name" to create a profile)', required = True)
    parser.add_argument('--to', dest = 'dest', metavar = '<aws-profile>', help='profile name for the target aws account (use "aws configure --profile name" to create a profile)', required = True)
    args = parser.parse_args()
    copy_database(args.src, args.dest, *args.databases)
    
if __name__ == '__main__':
   main()
