# -*- encoding: utf-8 -*-
# stub: minima 2.5.2 ruby lib

Gem::Specification.new do |s|
  s.name = "minima".freeze
  s.version = "2.5.2"

  s.required_rubygems_version = Gem::Requirement.new(">= 0".freeze) if s.respond_to? :required_rubygems_version=
  s.metadata = { "plugin_type" => "theme" } if s.respond_to? :metadata=
  s.require_paths = ["lib".freeze]
  s.authors = ["Joel Glovier".freeze]
  s.date = "2024-09-06"
  s.email = ["jglovier@github.com".freeze]
  s.homepage = "https://github.com/jekyll/minima".freeze
  s.licenses = ["MIT".freeze]
  s.required_ruby_version = Gem::Requirement.new(">= 2.7.0".freeze)
  s.rubygems_version = "3.3.27".freeze
  s.summary = "A beautiful, minimal theme for Jekyll.".freeze

  s.installed_by_version = "3.3.27" if s.respond_to? :installed_by_version

  if s.respond_to? :specification_version then
    s.specification_version = 4
  end

  if s.respond_to? :add_runtime_dependency then
    s.add_runtime_dependency(%q<jekyll>.freeze, [">= 3.5", "< 5.0"])
    s.add_runtime_dependency(%q<jekyll-feed>.freeze, ["~> 0.9"])
    s.add_runtime_dependency(%q<jekyll-seo-tag>.freeze, ["~> 2.1"])
  else
    s.add_dependency(%q<jekyll>.freeze, [">= 3.5", "< 5.0"])
    s.add_dependency(%q<jekyll-feed>.freeze, ["~> 0.9"])
    s.add_dependency(%q<jekyll-seo-tag>.freeze, ["~> 2.1"])
  end
end
