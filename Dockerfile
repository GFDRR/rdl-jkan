FROM ruby:3.3

RUN gem update --system
RUN gem install bundler:4.0.3

RUN apt-get update \
 && apt-get install -y --quiet --no-install-recommends \
 nodejs npm build-essential ruby-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /srv/jekyll

COPY Gemfile Gemfile.lock ./

RUN bundle config set --local frozen true
RUN bundle install

RUN git config --global --add safe.directory /srv/jekyll

CMD ["/bin/bash"]
