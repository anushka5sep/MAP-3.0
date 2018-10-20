import React from "react";
import {
  Card,
  CardHeader,
  CardBody,
  CardTitle,
  Row,
  Col
} from "reactstrap";

class Dashboard extends React.Component {
  render() {
    return (
      <div className="content">
        <Row>
          <Col xs={12}>
            <Card>
              <CardHeader>
                <CardTitle>Users Expression</CardTitle>
                <p className="card-category">MAP 3.0</p>
              </CardHeader>
              <CardBody>
            
              </CardBody>
            </Card>
          </Col>
        </Row>       
      </div>
    );
  }
}

export default Dashboard;
