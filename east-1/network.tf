resource "aws_internet_gateway" "prod-igw" {
    vpc_id = "${aws_vpc.vpc.id}"
}

resource "aws_route_table" "prod-public-crt" {
    vpc_id = "${aws_vpc.vpc.id}"
    
    route {
        //associated subnet can reach everywhere
        cidr_block = "0.0.0.0/0" 
        //CRT uses this IGW to reach internet
        gateway_id = "${aws_internet_gateway.prod-igw.id}" 
    }
    
}

resource "aws_route" "internet_access" {
    route_table_id         = aws_vpc.vpc.main_route_table_id
    destination_cidr_block = "0.0.0.0/0"
    gateway_id             = aws_internet_gateway.prod-igw.id
    
}

#resource "aws_route_table_association" "prod-crta-public-subnet-1"{
#    subnet_id = "${aws_subnet.prod-subnet-public-1.id}"
#    route_table_id = "${aws_route_table.prod-public-crt.id}"
#}
#
#resource "aws_route_table_association" "prod-crta-public-subnet-2"{
#    subnet_id = "${aws_subnet.prod-subnet-public-2.id}"
#    route_table_id = "${aws_route_table.prod-public-crt.id}"
#}
#
#resource "aws_route_table_association" "prod-crta-public-subnet-3"{
#    subnet_id = "${aws_subnet.prod-subnet-public-3.id}"
#    route_table_id = "${aws_route_table.prod-public-crt.id}"
#}
#
#resource "aws_route_table_association" "prod-crta-public-subnet-4"{
#    subnet_id = "${aws_subnet.prod-subnet-public-4.id}"
#    route_table_id = "${aws_route_table.prod-public-crt.id}"
#}