---
attributions:
- entity:
    affiliation: null
    email: null
    name: Joint Research Centre
    url: https://data.humdata.org/dataset/tropical-cyclone-irma-17-path-and-wind-speed-zones-as-of-7-september-2017
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/tropical-cyclone-irma-17-path-and-wind-speed-zones-as-of-7-september-2017
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/tropical-cyclone-irma-17-path-and-wind-speed-zones-as-of-7-september-2017
dataset_id: rdls_hzd-unosat_tropicalcycloneirma17path_20170907
description: 'This dataset illustrates the tropical cyclone IRMA-17 path with low,
  medium and strong wind impact zones observed and predicted at 7 September 2017.
  The tropical cyclone path and wind speed zones were derived from Joint Research
  Centre data (Warning 33 issued the 07 th September 2017 at 09:00 UTC). This is a
  preliminary analysis and has not yet been validated in the field.. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/tropical-cyclone-irma-17-path-and-wind-speed-zones-as-of-7-september-2017]'
details: This is a preliminary analysis and has not yet been validated in the field.
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
  description: Tropical cyclone IRMA-17 track and wind speed zones were derived from
    Joint Research Centre observational data and forecasts (Warning 33, 7 September
    2017 09:00 UTC). The dataset represents observed and predicted cyclone path geometry
    with classified wind impact zones (low, medium, strong) at a single time snapshot,
    providing preliminary hazard characterization prior to field validation.
  sources:
  - id: source_1
    license: null
    name: Joint Research Centre
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/tropical-cyclone-irma-17-path-and-wind-speed-zones-as-of-7-september-2017
  rel: source
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: Direct Observational Data/Anecdotal Data
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Tropical Cyclone IRMA-17 : Path and Wind Speed Zones (Shapefile)'
  download_url: https://data.humdata.org/dataset/13d54496-4f75-4e32-898f-62d015bff86c/resource/903ed1fe-2d86-4bef-aff6-8499a739ce95/download/irma_unosat_7sept.zip
  format: null
  id: resource_903ed1fe
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Irma_unosat_7Sept.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-unosat_tropicalcycloneirma17path_20170907
spatial:
  bbox: null
  centroid: null
  countries:
  - USA
  - ATG
  - BRB
  - DMA
  - DOM
  - GRL
  - HTI
  - JAM
  - KNA
  - LCA
  - PRI
  - TCA
  - VCT
  - VGB
  - VIR
  gazetteer_entries: []
  scale: regional
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2017-09-07'
temporal_resolution: null
title: 'Tropical Cyclone IRMA-17 : Path and Wind Speed Zones'
version: null
vulnerability: null
---
