---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: null
  name: Aqueduct
  url: https://www.wri.org/data/aqueduct-global-maps-40-data
creator:
  affiliation: null
  email: null
  name: Aqueduct
  url: https://www.wri.org/data/aqueduct-global-maps-40-data
dataset_id: rdls_exp-crstac_currentandfutureglobalmapsdataaqueduct40_waterstressfuture
description: 'Aqueduct Baseline Water Stress from 2030-2080, provided at sub-basin
  scale. Climate scenarios (as published): "SSP-RCP combinations" [Source: This metadata
  record was automatically extracted from the STAC catalog climate-risk-stac (https://climate-risk-data.github.io/climate-risk-stac/)]'
details: null
exposure:
- asset_type:
    description: land use/land cover footprints
    id: natural_environment
    scheme: null
    title: null
    uri: null
  category: natural_environment
  id: exposure_1
  metrics:
  - dimension: product
    id: metric_1
    measurement:
      quantity_kind: area
      unit: square_metre
hazard: null
license: https://spdx.org/licenses/CC-BY-4.0.html
lineage:
  description: "This dataset provides users with Aqueduct\xE2\u201E\xA2 4.0, the latest\
    \ iteration of WRI's water risk framework designed to translate complex hydrological\
    \ data into intuitive indicators of water-related risk. It consists of 13 baseline\
    \ water risk indicators spanning quantity, quality, and reputational concerns.\
    \ Aqueduct 4.0 adds new future projections of water supply, demand, stress, depletion,\
    \ and variability based on CMIP6 climate projections for 3 milestone years: 2030,\
    \ 2050, and 2080."
  sources:
  - id: source_underlying_1
    license: null
    name: Several data sources (see methodology for further details)
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Aqueduct
  url: https://www.wri.org/data/aqueduct-global-maps-40-data
purpose: The water stress indicator is a proxy for competition on water, as it accounts
  for both multi-sectoral water demand, relative to the abundance of water. Aqueduct
  data is provided at sub-basin scale. These data can be interesected with the area
  of interest, so to derieve an aggregate value weighted by the relative area of each
  catchment with the area of interest.
referenced_by:
- author_names: null
  date_published: null
  doi: 10.46830/writn.23.00061
  id: ref_doi
  name: null
  url: https://doi.org/10.46830/writn.23.00061
resources:
- access_url: https://climate-risk-data.github.io/climate-risk-stac/stac/exposure-vulnerability/land-use/current-and-future-global-maps-data-aqueduct-40/water-stress-future/water-stress-future.json
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
  spatial_aggregation: hydrological sub-basins
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'STAC Item: Current and Future Global Maps Data (Aqueduct 4.0) - Water Stress
    future'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Current and Future Global Maps Data (Aqueduct 4.0) - Water Stress future
    - data file
  download_url: https://files.wri.org/aqueduct/aqueduct-4-0-water-risk-data.zip
  format: null
  id: resource_data-file_1
  media_type: application/zip
  spatial: null
  spatial_aggregation: hydrological sub-basins
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Current and Future Global Maps Data (Aqueduct 4.0) - Water Stress future
    - data file
- access_url: https://doi.org/10.46830/writn.23.00061
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Current and Future Global Maps Data (Aqueduct 4.0) - Water Stress future
    (Web reference)
  download_url: null
  format: Web reference
  id: resource_link_reference
  media_type: null
  spatial: null
  spatial_aggregation: hydrological sub-basins
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Reference
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-crstac_currentandfutureglobalmapsdataaqueduct40_waterstressfuture
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
  end: '2080'
  start: '2030'
temporal_resolution: P1M
title: Current and Future Global Maps Data (Aqueduct 4.0) - Water Stress future
version: null
vulnerability: null
---
