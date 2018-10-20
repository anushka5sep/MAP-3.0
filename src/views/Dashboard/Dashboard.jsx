import React from "react";
import {
  Card,
  CardHeader,
  CardBody,
  CardTitle,
  Row,
  Col
} from "reactstrap";
import Svg from "./Svg.jsx"

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
                <Svg data={[5,10,1,3,16,2,8,24,17,5,10,1,3,16,2,8,24,17]} size={[500,500]} />
              </CardBody>
            </Card>
          </Col>
        </Row>       
      </div>
    );
  }
}

export default Dashboard;
