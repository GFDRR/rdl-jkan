---
attributions:
- entity:
    affiliation: null
    email: null
    name: NOAA International Best Track Archive for Climate Stewardship (IBTrACS)
    url: https://data.humdata.org/dataset/viet-nam-storm-tracks
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: UN in Viet Nam
  url: https://data.humdata.org/dataset/viet-nam-storm-tracks
creator:
  affiliation: null
  email: null
  name: UN in Viet Nam
  url: https://data.humdata.org/dataset/viet-nam-storm-tracks
dataset_id: rdls_hzd-vnm_un_in_viet_nam_stormtracks_1980
description: 'The dataset consists of consolidated history of tropical storm paths
  over Viet Nam from 1980-2023. NOAA''s International Best Track Archive for Climate
  Stewardship (IBTrACS) data, accessed on 20 October 2023: https://www.ncei.noaa.gov/products/international-best-track-archive?name=rsmc-data.
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/viet-nam-storm-tracks]'
details: NOAA's International Best Track Archive for Climate Stewardship (IBTrACS)
  data, accessed on 20 October 2023.
exposure: []
hazard:
  event_sets_by_hazard_type:
    strong_wind:
    - analysis_type: empirical
      calculation_method: observed
      event_count: 0
      events: []
      frequency_distribution: null
      hazards:
      - classification: null
        id: hazard_1
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Historical tropical cyclone tracks over Vietnam were extracted from
    NOAA's IBTrACS database, which consolidates best-track data from multiple international
    meteorological agencies. The dataset contains observed storm positions, wind speeds
    (WMO and USA standards), central pressure, and structural parameters (wind radii)
    from 1980-2023, provided in shapefile and geopackage formats for spatial analysis.
  sources:
  - id: source_1
    license: null
    name: NOAA International Best Track Archive for Climate Stewardship (IBTrACS)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/viet-nam-storm-tracks
  rel: source
loss:
  losses: []
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: Registry
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This shape file consists of consolidated history of tropical storm
    paths over Viet Nam from 1980-2023.
  download_url: https://data.humdata.org/dataset/2a36548d-a9d2-4f1c-8290-77a675a43818/resource/7e31a39b-0533-4396-9f72-ea3edfe1880b/download/viet-nam-storms-shp.zip
  format: null
  id: resource_7e31a39b
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Viet Nam storms SHP.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Geopackage consists of consolidated history of tropical storm paths
    over Viet Nam from 1980-2023.
  download_url: https://data.humdata.org/dataset/2a36548d-a9d2-4f1c-8290-77a675a43818/resource/0aefe296-b90e-4a9a-ab30-a991a368fef1/download/viet-nam-storms-geopackage.zip
  format: null
  id: resource_0aefe296
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Viet Nam storms geopackage.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-vnm_un_in_viet_nam_stormtracks_1980
spatial:
  bbox: null
  centroid: null
  countries:
  - VNM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2023-10-20'
  start: '1980-01-01'
temporal_resolution: null
title: 'Viet Nam: Storm Tracks'
version: null
vulnerability: null
---
