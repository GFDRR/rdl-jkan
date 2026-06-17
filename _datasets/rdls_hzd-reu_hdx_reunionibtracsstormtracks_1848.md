---
attributions:
- entity:
    affiliation: null
    email: null
    name: National Oceanic and Atmospheric Administration (NOAA) / National Centers
      for Environmental Information (NCEI)
    url: https://data.humdata.org/dataset/reu-ibtracs-tropical-storm-tracks
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: HDX
  url: https://data.humdata.org/dataset/reu-ibtracs-tropical-storm-tracks
creator:
  affiliation: null
  email: null
  name: National Oceanic and Atmospheric Administration (NOAA) / National Centers
    for Environmental Information (NCEI)
  url: https://data.humdata.org/dataset/reu-ibtracs-tropical-storm-tracks
dataset_id: rdls_hzd-reu_hdx_reunionibtracsstormtracks_1848
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
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/reu-ibtracs-tropical-storm-tracks]'
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
  description: "IBTrACS integrates historical and recent tropical cyclone observations\
    \ from multiple national meteorological agencies into a unified best-track dataset.\
    \ Track positions, wind speeds (WMO standard), and central pressures are quality-controlled\
    \ and standardized. The R\xE9union subset contains all cyclone tracks affecting\
    \ or passing through the Indian Ocean basin region."
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
- href: https://data.humdata.org/dataset/reu-ibtracs-tropical-storm-tracks
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
  description: "IBTrACS storm tracks from 1848 to date that pass within 2000 kilometers\
    \ of R\xE9union."
  download_url: https://data.humdata.org/dataset/43f1eaec-eb90-421a-8b7d-6d277b019c1c/resource/1979df9d-083e-452d-876b-16ee4200d59f/download/ibtracs_all_list_v04r01_reu.csv
  format: null
  id: resource_1979df9d
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ibtracs_ALL_list_v04r01_REU.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "IBTrACS storm tracks from 1848 to date that pass within 2000 kilometers\
    \ of R\xE9union."
  download_url: https://data.humdata.org/dataset/43f1eaec-eb90-421a-8b7d-6d277b019c1c/resource/f592f3d0-17fc-4a34-8db9-4175ed7f9b9d/download/ibtracs_all_list_v04r01_lines_reu.geojson
  format: null
  id: resource_f592f3d0
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ibtracs_ALL_list_v04r01_lines_REU.geojson
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-reu_hdx_reunionibtracsstormtracks_1848
spatial:
  bbox: null
  centroid: null
  countries:
  - REU
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2026-01-21'
  start: '1848-01-11'
temporal_resolution: null
title: "R\xE9union: IBTrACS Storm Tracks"
version: null
vulnerability: null
---
