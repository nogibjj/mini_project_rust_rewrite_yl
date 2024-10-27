# Display Rust command-line utility versions
rust-version:
	@echo "Rust command-line utility versions:"
	rustc --version              # Rust compiler
	cargo --version              # Rust package manager
	rustfmt --version            # Rust code formatter
	rustup --version             # Rust toolchain manager
	clippy-driver --version      # Rust linter

# Format code using rustfmt
format:
	cargo fmt --quiet

# Run clippy for linting
lint:
	cargo clippy --quiet

# Run tests
test:
	cargo test --quiet

# Build and run the project
run:
	cargo run

# Build release version
release:
	cargo build --release

# Install Rust toolchain if needed
install:
	# Install if needed
	# @echo "Updating rust toolchain"
	# rustup update stable
	# rustup default stable 

# Run all formatting, linting, and testing tasks
all: format lint test run

# Custom tasks

# Example: Extract data
extract: 
	cargo run extract

# Example: Transform and Load data
transform_load:
	cargo run transform_load

# Example: Create a database entry
create:
	cargo run query "INSERT INTO candy_data_DB (competitorname, chocolate, fruity, caramel, peanutyalmondy, nougat, crispedricewafer, hard, bar, pluribus) VALUES ('Grand Rabbit', 0, 0, 0, 0, 0, 0, 0, 0, 0);"

# Example: Read from the database
read:
	cargo run query "SELECT * FROM candy_data_DB WHERE competitorname = 'Grand Rabbit';"

# Example: Update a database entry
update:
	cargo run query "UPDATE candy_data_DB SET competitorname='Grand Rabbit', chocolate=0, fruity=1, caramel=0, peanutyalmondy=0, nougat=0, crispedricewafer=0, hard=0, bar=0, pluribus=0 WHERE id=86;"

# Example: Delete a database entry
delete:
	cargo run query "DELETE FROM candy_data_DB WHERE id=86;"

# Generate and push changes to GitHub
generate_and_push:
	@if [ -n "$$(git status --porcelain)" ]; then \
		git config --local user.email "action@github.com"; \
		git config --local user.name "GitHub Action"; \
		git add .; \
		git commit -m "Add query log"; \
		git push; \
	else \
		echo "No changes to commit. Skipping commit and push."; \
	fi