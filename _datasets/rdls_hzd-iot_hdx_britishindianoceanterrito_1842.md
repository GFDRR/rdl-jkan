---
attributions:
- entity:
    affiliation: null
    email: null
    name: National Oceanic and Atmospheric Administration (NOAA) / National Centers
      for Environmental Information (NCEI)
    url: https://data.humdata.org/dataset/iot-ibtracs-tropical-storm-tracks
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: HDX
  url: https://data.humdata.org/dataset/iot-ibtracs-tropical-storm-tracks
creator:
  affiliation: null
  email: null
  name: National Oceanic and Atmospheric Administration (NOAA) / National Centers
    for Environmental Information (NCEI)
  url: https://data.humdata.org/dataset/iot-ibtracs-tropical-storm-tracks
dataset_id: rdls_hzd-iot_hdx_britishindianoceanterrito_1842
description: 'The International Best Track Archive for Climate Stewardship (IBTrACS)
  project is the most complete global collection of tropical cyclones available. It
  merges recent and historical tropical cyclone data from multiple agencies to create
  a unified, publicly available, best-track dataset that improves inter-agency comparisons.
  Fields available: SID: A unique storm identifier (SID) assigned by IBTrACS algorithm.
  ISO_TIME: Time of the observation in ISO format (YYYY-MM-DD hh:mm:ss) BASIN: Basin
  of the current storm position SUBBASIN: Sub-basin of the current storm position
  NATURE: Type of storm (a combination of the various types from the available sources)
  NUMBER: Number of the storm for the year (restarts at 1 for each year LAT: Mean
  position - latitude (a combination of the available positions) LON: Mean position
  - longitude (a combination of the available positions) WMO_WIND: Maximum sustained
  wind speed assigned by the responsible WMO agency WMO_PRES: Minimum central pressure
  assigned by the responsible WMO agency.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/iot-ibtracs-tropical-storm-tracks]'
details: 'Some early (pre-1950) storms were not correctly matched, so the number of
  storms in the record is artificially high. For example, SIO storms in 1901 are not
  matched, so the same storm is tracked by the following identifiers: ds824, td9636,
  and reunion. This storm is broken into different tracks because of temporal differences
  in the storm data.'
exposure: []
hazard:
  event_sets:
  - analysis_type: probabilistic
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
  type: strong_wind
license: CC-BY-4.0
lineage:
  description: IBTrACS merges historical and recent tropical cyclone observations
    from multiple national meteorological agencies into a unified best-track dataset.
    Track positions, wind speeds (wmo_wind), and central pressures (wmo_pres) are
    standardized and quality-controlled. The dataset provides observed hazard characteristics
    for tropical cyclones affecting the British Indian Ocean Territory region.
  sources:
  - id: source_1
    license: null
    name: National Oceanic and Atmospheric Administration (NOAA) / National Centers
      for Environmental Information (NCEI)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/iot-ibtracs-tropical-storm-tracks
  rel: source
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: null
referenced_by:
- author_names: null
  date_published: null
  doi: null
  id: reference_1
  name: Methodology documentation
  url: https://www.ncei.noaa.gov/sites/g/files/anmtlf171/files/2024-07/IBTrACS_version4r01_Technical_Details.pdf
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: IBTrACS storm tracks from 1842 to date that pass within 2000 kilometers
    of British Indian Ocean Territory.
  download_url: https://data.humdata.org/dataset/544ba5f5-1e68-4ead-8391-c2b39fcb10c4/resource/a111242f-8d82-472b-96cc-a400854dc592/download/ibtracs_all_list_v04r01_iot.csv
  format: null
  id: resource_a111242f
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ibtracs_ALL_list_v04r01_IOT.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: IBTrACS storm tracks from 1842 to date that pass within 2000 kilometers
    of British Indian Ocean Territory.
  download_url: https://data.humdata.org/dataset/544ba5f5-1e68-4ead-8391-c2b39fcb10c4/resource/a2fc7e6e-805f-4bed-8291-1996b9f3d070/download/ibtracs_all_list_v04r01_lines_iot.geojson
  format: null
  id: resource_a2fc7e6e
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ibtracs_ALL_list_v04r01_lines_IOT.geojson
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-iot_hdx_britishindianoceanterrito_1842
spatial:
  bbox: null
  centroid: null
  countries:
  - IOT
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2026-01-21'
  start: '1842-10-25'
temporal_resolution: null
title: 'British Indian Ocean Territory: IBTrACS Storm Tracks'
version: null
vulnerability: null
---
