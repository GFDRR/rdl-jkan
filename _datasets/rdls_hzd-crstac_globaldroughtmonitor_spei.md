---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: null
  name: Spanish National Research Council (CSIC)
  url: https://spei.csic.es/map/maps.html#months=1#month=5#year=2024
creator:
  affiliation: null
  email: null
  name: Spanish National Research Council (CSIC)
  url: https://spei.csic.es/map/maps.html#months=1#month=5#year=2024
dataset_id: rdls_hzd-crstac_globaldroughtmonitor_spei
description: 'SPEI Global Drought Monitor is based on the Thortnthwaite equation for
  estimating potential evapotranspiration, PET [Source: This metadata record was automatically
  extracted from the STAC catalog climate-risk-stac (https://climate-risk-data.github.io/climate-risk-stac/)]'
details: null
exposure: []
hazard:
  event_sets_by_hazard_type:
    drought:
    - analysis_type: deterministic
      calculation_method: simulated
      event_count: 0
      events: []
      frequency_distribution: null
      hazards:
      - classification: null
        id: hazard_1
        intensity_measure: spi:dimensionless
        process: meteorological_drought
        trigger: null
        type: drought
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://spdx.org/licenses/ODbL-1.0.html
lineage:
  description: The SPEI Global Drought Monitor offers near real-time information about
    drought conditions at the global scale, with a 1 degree spatial resolution and
    a monthly time resolution. SPEI time-scales between 1 and 48 months are provided.
  sources:
  - id: source_underlying_1
    license: null
    name: NOAA
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
loss:
  losses: []
project: null
publisher:
  affiliation: null
  email: null
  name: Spanish National Research Council (CSIC)
  url: https://spei.csic.es/map/maps.html#months=1#month=5#year=2024
purpose: data download via interface
referenced_by: []
resources:
- access_url: https://climate-risk-data.github.io/climate-risk-stac/stac/hazard/precipitation-related/global-drought-monitor/spei/spei.json
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
  title: 'STAC Item: Global Drought Monitor - SPEI'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Global Drought Monitor - SPEI - data file
  download_url: https://spei.csic.es/map/maps.html#months=1#month=5#year=2024
  format: null
  id: resource_data-file_1
  media_type: application/x-netcdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Global Drought Monitor - SPEI - data file
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-crstac_globaldroughtmonitor_spei
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
spatial_resolution: 111000
temporal:
  central_year: null
  duration: null
  end: '2026'
  start: '1955'
temporal_resolution: P1M
title: Global Drought Monitor - SPEI
version: null
vulnerability: null
---
