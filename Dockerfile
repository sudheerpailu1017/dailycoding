
ARG JAVA_VERSION="17-jdk"

FROM openjdk:${JAVA_VERSION}

COPY target/spring_rest-backend-0.0.1-SNAPSHOT.jar spring_rest-backend-1.1.jar

EXPOSE 8080

ENTRYPOINT ["java", "-jar", "spring_rest-backend-1.1.jar"]