---
catalog: Humanitarian Data Exchange
contact_point:
  email: null
  id: attribution_contact
  name: HDX
  url: https://data.humdata.org/dataset/6049e2a0-2e1a-4cdb-85e9-868c468d3e22
creator:
  email: null
  id: attribution_creator
  name: National Oceanic and Atmospheric Administration (NOAA) / National Centers
    for Environmental Information (NCEI)
  url: https://data.humdata.org/dataset/6049e2a0-2e1a-4cdb-85e9-868c468d3e22
dataset_id: rdls_hzd-hdx_hdx_ton_ton_ibtracs_tropical_storm_tracks_windstorm
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
  assigned by the responsible WMO agency. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX) at https://data.humdata.org]
  [Original dataset: https://data.humdata.org/dataset/6049e2a0-2e1a-4cdb-85e9-868c468d3e22]'
details: 'Caveats: Some early (pre-1950) storms were not correctly matched, so the
  number of storms in the record is artificially high. For example, SIO storms in
  1901 are not matched, so the same storm is tracked by the following identifiers:
  ds824, td9636, and reunion. This storm is broken into different tracks because of
  temporal differences in the storm data. | Methodology: Please find the methodology
  at [this link](https://www.ncei.noaa.gov/sites/g/files/anmtlf171/files/2024-07/IBTrACS_version4r01_Technical_Details.pdf)
  | Temporal coverage: [1919-05-14T00:00:00 TO 2025-03-01T23:59:59] | Update frequency:
  As needed | Last modified: 2025-08-26'
exposure: []
extra_attributions: []
hazard:
  calculation_method: observed
  disaster_identifiers: ''
  hazard_analysis_type: empirical
  hazard_type: convective_storm
  intensity: sws_10m:m/s
  occurrence_range: ''
  processes: tornado
  seasonality: ''
license: Creative Commons Attribution for Intergovernmental Organisations (CC BY-IGO)
loss: null
project: null
publisher:
  email: null
  id: attribution_publisher
  name: HDX
  url: https://data.humdata.org/dataset/6049e2a0-2e1a-4cdb-85e9-868c468d3e22
purpose: null
resources:
- coordinate_system: null
  description: Dataset-level metadata exported from HDX.
  download_url: https://data.humdata.org/dataset/6049e2a0-2e1a-4cdb-85e9-868c468d3e22/download_metadata?format=json
  format: JSON (json)
  id: hdx_dataset_metadata_json
  media_type: null
  spatial_resolution: null
  temporal: null
  title: HDX dataset metadata (JSON)
- coordinate_system: null
  description: IBTrACS storm tracks from 1919 to date that pass within 2000 kilometers
    of Tonga.
  download_url: https://data.humdata.org/dataset/6049e2a0-2e1a-4cdb-85e9-868c468d3e22/resource/70ed16b9-2202-4069-9a93-2c772b47c4b3/download/ibtracs_all_list_v04r01_ton.csv
  format: CSV (csv)
  id: hdx_res_70ed16b9
  media_type: null
  spatial_resolution: null
  temporal: null
  title: ibtracs_ALL_list_v04r01_TON.csv
- coordinate_system: null
  description: IBTrACS storm tracks from 1919 to date that pass within 2000 kilometers
    of Tonga.
  download_url: https://data.humdata.org/dataset/6049e2a0-2e1a-4cdb-85e9-868c468d3e22/resource/08815b30-fda6-42b2-9030-d3ea8a9cb7ce/download/ibtracs_all_list_v04r01_lines_ton.geojson
  format: GeoJSON (geojson)
  id: hdx_res_08815b30
  media_type: null
  spatial_resolution: null
  temporal: null
  title: ibtracs_ALL_list_v04r01_lines_TON.geojson
risk_data_type:
- hazard
schema: rdl-03
slug: rdls_hzd-hdx_hdx_ton_ton_ibtracs_tropical_storm_tracks_windstorm
spatial:
  countries:
  - TON
  scale: national
title: 'Tonga: IBTrACS Storm Tracks'
version: null
vulnerability: null
---
