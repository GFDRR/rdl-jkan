---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: null
  name: Figshare
  url: https://figshare.com/s/9a94ae958d6a45684382
creator:
  affiliation: null
  email: null
  name: Figshare
  url: https://figshare.com/s/9a94ae958d6a45684382
dataset_id: rdls_exp-crstac_coastalpopulationprojections_projections
description: 'Coastal population projections under the Shared Socioeconomic Pathways
  (SSPs) until 2100. Climate scenarios (as published): "SSPs" [Source: This metadata
  record was automatically extracted from the STAC catalog climate-risk-stac (https://climate-risk-data.github.io/climate-risk-stac/)]'
details: null
exposure:
- asset_type:
    description: population number
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_1
  metrics:
  - dimension: population
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard: null
license: https://spdx.org/licenses/CC-BY-4.0.html
lineage:
  description: Coastal population projections under the Shared Socioeconomic Pathways
    (SSPs) until 2100
  sources:
  - id: source_underlying_1
    license: null
    name: GRUMP population and urban settlements data
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
loss:
  losses: []
project: null
publisher:
  affiliation: null
  email: null
  name: Figshare
  url: https://figshare.com/s/9a94ae958d6a45684382
purpose: The projections were developed with coastal applications in mind
referenced_by:
- author_names: null
  date_published: null
  doi: 10.1016/j.gloplacha.2016.08.009
  id: ref_doi
  name: null
  url: https://doi.org/10.1016/j.gloplacha.2016.08.009
resources:
- access_url: https://climate-risk-data.github.io/climate-risk-stac/stac/exposure-vulnerability/population/coastal-population-projections/projections/projections.json
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
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'STAC Item: Projections'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Projections - data file
  download_url: https://figshare.com/ndownloader/articles/3201130?private_link=9a94ae958d6a45684382
  format: null
  id: resource_data-file_1
  media_type: image/tiff; application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Projections - data file
- access_url: https://doi.org/10.1016/j.gloplacha.2016.08.009
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Projections (Web reference)
  download_url: null
  format: Web reference
  id: resource_link_reference
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Reference
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-crstac_coastalpopulationprojections_projections
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
spatial_resolution: 926
temporal:
  central_year: null
  duration: null
  end: '2100'
  start: '2005'
temporal_resolution: P5Y
title: Projections
version: null
vulnerability: null
---
