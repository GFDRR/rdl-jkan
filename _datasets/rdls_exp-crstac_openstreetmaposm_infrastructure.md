---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: null
  name: Open street map
  url: https://www.openstreetmap.org/
creator:
  affiliation: null
  email: null
  name: Open street map
  url: https://www.openstreetmap.org/
dataset_id: rdls_exp-crstac_openstreetmaposm_infrastructure
description: 'OpenStreetMap is a free, editable map of the whole world that is being
  built by volunteers largely from scratch and released with an open-content license
  [Source: This metadata record was automatically extracted from the STAC catalog
  climate-risk-stac (https://climate-risk-data.github.io/climate-risk-stac/)]'
details: null
exposure:
- asset_type:
    description: infrastructure footprints
    id: infrastructure
    scheme: null
    title: null
    uri: null
  category: infrastructure
  id: exposure_1
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard: null
license: https://spdx.org/licenses/ODbL-1.0.html
lineage:
  description: OpenStreetMap is a free, editable map of the whole world that is being
    built by volunteers largely from scratch and released with an open-content license.
  sources:
  - id: source_code_codelink
    license: null
    name: Code link
    risk_data_type: null
    type: model
    url: https://github.com/osm-flex/osm-flex
    used_in: null
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
loss:
  losses: []
project: null
publisher:
  affiliation: null
  email: null
  name: Open street map
  url: https://www.openstreetmap.org/
purpose: The development of OSM is community led. Therefore, completeness of the data
  differs across countries.
referenced_by: []
resources:
- access_url: https://climate-risk-data.github.io/climate-risk-stac/stac/exposure-vulnerability/infrastructure/open-street-map-osm/infrastructure/infrastructure.json
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Source STAC Item metadata record for this dataset, hosted as part of
    the climate-risk-stac catalogue. Conforms to STAC v1.0.0.
  download_url: null
  format: null
  id: resource_stac_item
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: feature level
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'STAC Item: Open Street Map (OSM) - Infrastructure'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Open Street Map (OSM) - Infrastructure - data file
  download_url: https://download.geofabrik.de/
  format: null
  id: resource_data-file_1
  media_type: application/x-protobuf
  spatial: null
  spatial_aggregation: feature level
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Open Street Map (OSM) - Infrastructure - data file
- access_url: https://github.com/osm-flex/osm-flex
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Open Street Map (OSM) - Infrastructure (Code link)
  download_url: null
  format: Web reference
  id: resource_link_codelink
  media_type: null
  spatial: null
  spatial_aggregation: feature level
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Code link
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-crstac_openstreetmaposm_infrastructure
spatial:
  bbox:
  - -180.0
  - -90.0
  - 180.0
  - 90.0
  centroid: null
  countries:
  - GLO
  gazetteer_entries: []
  scale: global
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2026'
  start: '2004'
temporal_resolution: null
title: Open Street Map (OSM) - Infrastructure
version: null
vulnerability: null
---
