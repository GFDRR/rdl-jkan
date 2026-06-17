---
attributions:
- entity:
    affiliation: null
    email: null
    name: National Oceanic and Atmospheric Administration (NOAA) / National Centers
      for Environmental Information (NCEI)
    url: https://data.humdata.org/dataset/sjm-ibtracs-tropical-storm-tracks
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: HDX
  url: https://data.humdata.org/dataset/sjm-ibtracs-tropical-storm-tracks
creator:
  affiliation: null
  email: null
  name: National Oceanic and Atmospheric Administration (NOAA) / National Centers
    for Environmental Information (NCEI)
  url: https://data.humdata.org/dataset/sjm-ibtracs-tropical-storm-tracks
dataset_id: rdls_hzd-sjm_hdx_svalbardjanmayenislandsib_1853
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
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/sjm-ibtracs-tropical-storm-tracks]'
details: 'Some early (pre-1950) storms were not correctly matched, so the number of
  storms in the record is artificially high. For example, SIO storms in 1901 are not
  matched, so the same storm is tracked by the following identifiers: ds824, td9636,
  and reunion. This storm is broken into different tracks because of temporal differences
  in the storm data.'
exposure: []
hazard:
  event_sets:
  - analysis_type: empirical
    calculation_method: observed
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: wmo_wind:m/s
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
    recorded at regular time intervals and quality-controlled. This regional subset
    contains all tropical cyclone tracks affecting Svalbard and Jan Mayen Islands.
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
- href: https://data.humdata.org/dataset/sjm-ibtracs-tropical-storm-tracks
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
  description: IBTrACS storm tracks from 1853 to date that pass within 2000 kilometers
    of Svalbard and Jan Mayen Islands.
  download_url: https://data.humdata.org/dataset/099af7cb-ddb5-4ec0-8838-5a8765b64d48/resource/4e1a6592-13d5-438c-a6b0-e4b16a63dc3e/download/ibtracs_all_list_v04r01_sjm.csv
  format: null
  id: resource_4e1a6592
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ibtracs_ALL_list_v04r01_SJM.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: IBTrACS storm tracks from 1853 to date that pass within 2000 kilometers
    of Svalbard and Jan Mayen Islands.
  download_url: https://data.humdata.org/dataset/099af7cb-ddb5-4ec0-8838-5a8765b64d48/resource/aa687e67-3d5e-4e0a-bec6-0908be235cec/download/ibtracs_all_list_v04r01_lines_sjm.geojson
  format: null
  id: resource_aa687e67
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ibtracs_ALL_list_v04r01_lines_SJM.geojson
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-sjm_hdx_svalbardjanmayenislandsib_1853
spatial:
  bbox: null
  centroid: null
  countries:
  - SJM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2023-09-26'
  start: '1853-08-30'
temporal_resolution: null
title: 'Svalbard and Jan Mayen Islands: IBTrACS Storm Tracks'
version: null
vulnerability: null
---
