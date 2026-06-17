---
attributions:
- entity:
    affiliation: null
    email: null
    name: National Oceanic and Atmospheric Administration (NOAA) / National Centers
      for Environmental Information (NCEI)
    url: https://data.humdata.org/dataset/vct-ibtracs-tropical-storm-tracks
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: HDX
  url: https://data.humdata.org/dataset/vct-ibtracs-tropical-storm-tracks
creator:
  affiliation: null
  email: null
  name: National Oceanic and Atmospheric Administration (NOAA) / National Centers
    for Environmental Information (NCEI)
  url: https://data.humdata.org/dataset/vct-ibtracs-tropical-storm-tracks
dataset_id: rdls_hzd-vct_hdx_saintvincentgrenadinesibt_1851
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
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/vct-ibtracs-tropical-storm-tracks]'
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
  description: IBTrACS aggregates tropical cyclone observations from multiple international
    agencies into a unified best-track dataset. The Saint Vincent and the Grenadines
    subset contains historical and recent storm tracks with ISO-formatted timestamps,
    basin/sub-basin classifications, wind speed (wmo_wind), and pressure (wmo_pres)
    measurements at observed locations.
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
- href: https://data.humdata.org/dataset/vct-ibtracs-tropical-storm-tracks
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
  description: IBTrACS storm tracks from 1851 to date that pass within 2000 kilometers
    of Saint Vincent and the Grenadines.
  download_url: https://data.humdata.org/dataset/9e44fd2a-1413-48a1-a506-08b4ea8cc14a/resource/fd41b980-43fa-486b-a64b-0a460a4cd842/download/ibtracs_all_list_v04r01_vct.csv
  format: null
  id: resource_fd41b980
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ibtracs_ALL_list_v04r01_VCT.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: IBTrACS storm tracks from 1851 to date that pass within 2000 kilometers
    of Saint Vincent and the Grenadines.
  download_url: https://data.humdata.org/dataset/9e44fd2a-1413-48a1-a506-08b4ea8cc14a/resource/1d33f766-2c58-48be-961b-b577c2b22368/download/ibtracs_all_list_v04r01_lines_vct.geojson
  format: null
  id: resource_1d33f766
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ibtracs_ALL_list_v04r01_lines_VCT.geojson
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-vct_hdx_saintvincentgrenadinesibt_1851
spatial:
  bbox: null
  centroid: null
  countries:
  - VCT
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2025-10-31'
  start: '1851-07-10'
temporal_resolution: null
title: 'Saint Vincent and the Grenadines: IBTrACS Storm Tracks'
version: null
vulnerability: null
---
