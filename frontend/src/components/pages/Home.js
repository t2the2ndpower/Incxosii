import React from "react";
import Hero from "../Hero";
import Container from "../Container";
import Row from "../Row";
import Col from "../Col";
import MainImage from "../images/main.png"


function Home() {
  return (
    <div>
      <Hero backgroundImage={MainImage}>
        <h1>Incxosi</h1>
        <h2>A one to one coaching platform for those who like to help others</h2>
      </Hero>
      <Container style={{ marginTop: 30 }}>
        <Row>
          <Col size="md-12">
          </Col>
        </Row>
        <Row>
          <Col size="md-12">
            <p>
              Have you ever wanted to help a friend with something that came natural to you but seemed to be a challenge for them?
            </p>
            <p>
              Have you gained life experience, overcome an obstacle, or received training and would like to pass this on?
            </p>
            <p>
              Incxosi allows those with knowledge to share it, in a one on one,incremental, measures based manner with accountability baked in.
            </p>
            <p>
              As a Teacher, Incxosi allows the Teacher user to create mini courses that are broken down into daily activities that span over 3, 6, or 12 weeks. These dailiy activities are automatically delivered to the student at preset times that the Incxosi set. As the student completes their daily activity, they respond via text or email. The response is tracked in the system and responses are then aggregated and delivered to the Incxosi's dashboard for overall student engagement accountability.
            </p>
          </Col>
        </Row>
      </Container>
    </div>
  );
}

export default Home;
