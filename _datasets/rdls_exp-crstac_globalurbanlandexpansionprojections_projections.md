---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: null
  name: Pangaea
  url: https://doi.org/10.1594/PANGAEA.905890
creator:
  affiliation: null
  email: null
  name: Pangaea
  url: https://doi.org/10.1594/PANGAEA.905890
dataset_id: rdls_exp-crstac_globalurbanlandexpansionprojections_projections
description: 'The data present the scenario projections of global urban land expansion
  under the framework of the shared socioeconomic pathways (SSPs) every 10 years from
  2015 to 2100. Our projections feature a fine spatial resolution of 1 km that preserves
  spatial details and avoids potential distortions in urban land patterns. Climate
  scenarios (as published): "SSPs" [Source: This metadata record was automatically
  extracted from the STAC catalog climate-risk-stac (https://climate-risk-data.github.io/climate-risk-stac/)]'
details: null
exposure:
- asset_type:
    description: urban/built-up footprints
    id: buildings
    scheme: null
    title: null
    uri: null
  category: buildings
  id: exposure_1
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: area
      unit: square_metre
hazard: null
license: https://spdx.org/licenses/CC-BY-NC-SA-4.0.html
lineage:
  description: The data present the scenario projections of global urban land expansion
    under the framework of the shared socioeconomic pathways (SSPs) every 10 years
    from 2015 to 2100. Our projections feature a fine spatial resolution of 1 km that
    preserves spatial details and avoids potential distortions in urban land patterns.
  sources:
  - id: source_underlying_1
    license: null
    name: GHSL and other
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
  name: Pangaea
  url: https://doi.org/10.1594/PANGAEA.905890
purpose: null
referenced_by:
- author_names: null
  date_published: null
  doi: 10.1038/s41467-020-14386-x
  id: ref_doi
  name: null
  url: https://doi.org/10.1038/s41467-020-14386-x
resources:
- access_url: https://climate-risk-data.github.io/climate-risk-stac/stac/exposure-vulnerability/land-use/global-urban-land-expansion-projections/projections/projections.json
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
  download_url: https://hs.pangaea.de/Maps/ChenG-etal_2019/Global-urban-product_SSPs_2015_2100.zip
  format: null
  id: resource_data-file_1
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Projections - data file
- access_url: https://doi.org/10.1038/s41467-020-14386-x
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
slug: rdls_exp-crstac_globalurbanlandexpansionprojections_projections
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
  start: '2015'
temporal_resolution: P10Y
title: Projections
version: null
vulnerability: null
---
