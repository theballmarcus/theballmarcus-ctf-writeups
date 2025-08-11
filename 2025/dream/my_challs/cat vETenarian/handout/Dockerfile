# Stage 1: Build the vulnerable binary
FROM alpine:latest AS builder

RUN apk add --no-cache gcc musl-dev

WORKDIR /ctf
COPY cat_vETenarian.c .
RUN gcc -static -fno-stack-protector cat_vETenarian.c -o cat_vETenarian

# Stage 2: Setup runtime environment and socat
FROM alpine:latest

RUN apk add --no-cache coreutils socat

WORKDIR /ctf
COPY --from=builder /ctf/cat_vETenarian .
COPY flag.txt .

# Expose port 7331 for the challenge
EXPOSE 7331

# Run socat to expose the binary on the port
CMD ["socat", "TCP-LISTEN:7331,reuseaddr,fork", "EXEC:/ctf/cat_vETenarian,pty,stderr"]
