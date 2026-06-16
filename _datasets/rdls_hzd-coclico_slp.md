---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: null
  name: Deltares
  url: https://deltares.nl
creator:
  affiliation: null
  email: null
  name: Deltares
  url: https://deltares.nl
dataset_id: rdls_hzd-coclico_slp
description: 'Sea level rise projections provide regional insights into future sea
  level changes, helping assess coastal flood risks and inform adaptation planning.
  Spatial coverage: Global Ocean and European seas Sources: IPCC AR6 report, Caron
  et al. Glacial Isostatic Adjustment (GIA), CMIP6 Common usage: Coastal impact assessment,
  adaptation planning, sensitivity analysis More info about the dataset can be found
  in the User Handbook. Variants in the source dataset - scenarios: high_end (High
  End), ssp126 (SSP1-2.6), ssp245 (SSP2-4.5), ssp585 (SSP5-8.5) - Climate scenarios
  based on IPCC''s Shared Socioeconomic Pathways (SSPs). High-end (if applicable)
  refers to P83 of SSP5-8.5, taking into account low-confidence processes. Other scenarios
  use the P50; ensemble: msl_h (83.3 Percentile), msl_m (50.0 Percentile), msl_l (16.7
  Percentile) - Uncertainty range of projections. 16.7, 50 and 83.3 indicate the lower
  bound, median and upper bound respectively; time: 2031 (2030), 2041 (2040), 2051
  (2050), 2061 (2060), 2071 (2070), 2081 (2080), 2091 (2090), 2101 (2100), ... (5
  more) - Time slice applied to the data. Either present-day (2010) or future state
  representing medium (2030 till 2050) and long term (2050 till 2100) outlook. [Source:
  This metadata record was automatically extracted from the STAC catalog coclico (https://www.openearth.nl/coclico-workbench/data_catalog/)]'
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
license: https://spdx.org/licenses/CC-BY-4.0.html
lineage:
  description: 'Sea level rise projections provide regional insights into future sea
    level changes, helping assess coastal flood risks and inform adaptation planning.
    Spatial coverage: Global Ocean and European seas Sources: IPCC AR6 report, Caron
    et al. Glacial Isostatic Adjustment (GIA), CMIP6 Common usage: Coastal impact
    assessment, adaptation planning, sensitivity analysis More info about the dataset
    can be found in the User Handbook'
  sources:
  - id: source_1
    license: null
    name: Deltares
    risk_data_type:
    - hazard
    type: dataset
    url: https://deltares.nl
    used_in: hazard
  - id: source_2
    license: null
    name: BRGM, French Geological Survey
    risk_data_type:
    - hazard
    type: dataset
    url: www.brgm.fr
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
  url: https://deltares.nl
purpose: null
referenced_by: []
resources:
- access_url: https://storage.googleapis.com/coclico-data-public/coclico/coclico-stac/slp/collection.json
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
  title: 'STAC Collection: CoCliCo - Sea Level Rise [slp]'
- access_url: https://storage.googleapis.com/coclico-data-public/coclico/assets/thumbnails/slp.png
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: CoCliCo - Sea Level Rise
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
slug: rdls_hzd-coclico_slp
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
title: CoCliCo - Sea Level Rise
version: null
vulnerability: null
---
