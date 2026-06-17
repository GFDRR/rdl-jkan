---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: null
  name: Deltares
  url: https://www.deltares.nl
creator:
  affiliation: null
  email: null
  name: Deltares
  url: https://www.deltares.nl
dataset_id: rdls_hzd-coclico_slp5
description: 'Regional sea level data from IPCC AR5 distributed in netCDF format by
  the Integrated Climate Data Center ICDC, CEN, University of Hamburg, Hamburg, Germany.
  [Source: This metadata record was automatically extracted from the STAC catalog
  coclico (https://www.openearth.nl/coclico-workbench/data_catalog/)]'
details: null
exposure: []
hazard:
  event_sets:
  - analysis_type: deterministic
    calculation_method: simulated
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: wd:m
      process: sea_level_rise
      trigger: null
      type: sea_level_rise
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: sea_level_rise
license: https://example.org/license/unknown
lineage:
  description: Regional sea level data from IPCC AR5 distributed in netCDF format
    by the Integrated Climate Data Center ICDC, CEN, University of Hamburg, Hamburg,
    Germany.
  sources:
  - id: source_1
    license: null
    name: Deltares
    risk_data_type:
    - hazard
    type: dataset
    url: https://www.deltares.nl
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Deltares
  url: https://www.deltares.nl
purpose: null
referenced_by: []
resources:
- access_url: https://storage.googleapis.com/coclico-data-public/coclico/coclico-stac/slp5/collection.json
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Source STAC Collection metadata for this dataset, hosted as part of
    the CoCliCo catalog. Conforms to STAC v1.0.0.
  download_url: null
  format: null
  id: resource_stac_collection
  media_type: application/json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'STAC Collection: CoCliCo - AR5 sea level rise projections [slp5]'
- access_url: https://storage.googleapis.com/coclico-data-public/coclico/assets/thumbnails/slp5.png
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: CoCliCo - AR5 sea level rise projections
  download_url: null
  format: null
  id: resource_thumbnail
  media_type: image/png
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Thumbnail
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-coclico_slp5
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
temporal: null
temporal_resolution: null
title: CoCliCo - AR5 sea level rise projections
version: null
vulnerability: null
---
