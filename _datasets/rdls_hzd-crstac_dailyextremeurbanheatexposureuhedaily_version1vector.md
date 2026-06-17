---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: null
  name: NASA
  url: https://doi.org/10.7927/fq7g-ny13
creator:
  affiliation: null
  email: null
  name: NASA
  url: https://doi.org/10.7927/fq7g-ny13
dataset_id: rdls_hzd-crstac_dailyextremeurbanheatexposureuhedaily_version1vector
description: 'High Resolution Daily Extreme Urban Heat Exposure, calculated for five
  combined temperture-humidity thresholds, shapefile vector data [Source: This metadata
  record was automatically extracted from the STAC catalog climate-risk-stac (https://climate-risk-data.github.io/climate-risk-stac/)]'
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
      intensity_measure: AirTemp:C
      process: extreme_heat
      trigger: null
      type: extreme_temperature
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: extreme_temperature
license: CC-BY-4.0
lineage:
  description: The Global High Resolution Daily Extreme Urban Heat Exposure (UHE-Daily),
    1983-2016 data set contains a high-resolution, longitudinal global record of geolocated
    urban extreme heat events and urban population exposure estimates for more than
    10,000 urban settlements worldwide for 1983-2016.
  sources:
  - id: source_underlying_1
    license: null
    name: CHIRTS-daily
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_code_codelink
    license: null
    name: Code link
    risk_data_type: null
    type: model
    url: https://github.com/ecohydro/GlobalUrbanHeat
    used_in: null
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: NASA
  url: https://doi.org/10.7927/fq7g-ny13
purpose: free user account needed
referenced_by:
- author_names: null
  date_published: null
  doi: 10.1073/pnas.2024792118
  id: ref_doi
  name: null
  url: https://doi.org/10.1073/pnas.2024792118
resources:
- access_url: https://climate-risk-data.github.io/climate-risk-stac/stac/hazard/temperature-related/daily-extreme-urban-heat-exposure-uhe-daily/version-1-vector/version-1-vector.json
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
  spatial_aggregation: city level
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'STAC Item: Daily Extreme Urban Heat Exposure (UHE-Daily) - version 1 vector'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Daily Extreme Urban Heat Exposure (UHE-Daily) - version 1 vector -
    data file
  download_url: https://data.earthdata.nasa.gov/nasa-earth/human-dimensions/sedac-root/downloads/data/sdei/sdei-high-res-daily-uhe-1983-2016/sdei-high-res-daily-uhe-1983-2016-shp.zip
  format: null
  id: resource_data-file_1
  media_type: application/x-shapefile
  spatial: null
  spatial_aggregation: city level
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Daily Extreme Urban Heat Exposure (UHE-Daily) - version 1 vector - data file
- access_url: https://doi.org/10.1073/pnas.2024792118
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Daily Extreme Urban Heat Exposure (UHE-Daily) - version 1 vector (Web
    reference)
  download_url: null
  format: Web reference
  id: resource_link_reference
  media_type: null
  spatial: null
  spatial_aggregation: city level
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Reference
- access_url: https://github.com/ecohydro/GlobalUrbanHeat
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Daily Extreme Urban Heat Exposure (UHE-Daily) - version 1 vector (Code
    link)
  download_url: null
  format: Web reference
  id: resource_link_codelink
  media_type: null
  spatial: null
  spatial_aggregation: city level
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Code link
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-crstac_dailyextremeurbanheatexposureuhedaily_version1vector
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
  end: '2016'
  start: '1983'
temporal_resolution: P1D
title: Daily Extreme Urban Heat Exposure (UHE-Daily) - version 1 vector
version: null
vulnerability: null
---
