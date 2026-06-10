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
dataset_id: rdls_hzd-coclico_cfhpall
description: 'Flood Maps represent the flood simulations across Europe (at 25 m resolution),
  indicating the maximum flood extent and depth, for different emission scenarios
  (including subsidence projections), storms, times and defense levels (if available).
  Spatial coverage: Europe Sources: protection levels (at NUTS2 level) if available,
  RFSM-EDA Common usage: flood mapping, urban planning, emergency response. More Info
  about the dataset: User Handbook. Variants in the source dataset - defense level:
  HIGH_DEFENDED_MAPS (High Defended), LOW_DEFENDED_MAPS (Low Defended), UNDEFENDED_MAPS
  (No Defense) - Policy-based coastal protection standards at the province level (NUTS2).
  High (low) defended: maximum (minimum) level of policy-based protection, if information
  is available. No defense: without protection (beyond what may be included in the
  DEM); rp: static (No Return Period), 1 (1 year), 100 (100 years), 1000 (1000 years)
  - Frequency at which an extreme event of total water level (related to storms) is
  expected to occur on average; scenarios: None (No Scenario), SSP126 (SSP1-2.6),
  SSP245 (SSP2-4.5), SSP585 (SSP5-8.5), High_End (High End) - Climate scenarios based
  on IPCC''s Shared Socioeconomic Pathways (SSPs). High-end (if applicable) refers
  to P83 of SSP5-8.5, taking into account low-confidence processes. Other scenarios
  use the P50; time: 2010, 2030, 2050, 2100 - Time slice applied to the data. Either
  present-day (2010) or future state representing medium (2030 till 2050) and long
  term (2050 till 2100) outlook. [Source: This metadata record was automatically extracted
  from the STAC catalog coclico (https://www.openearth.nl/coclico-workbench/data_catalog/)]'
details: null
exposure: []
hazard:
  event_sets:
  - analysis_type: probabilistic
    calculation_method: simulated
    event_count: null
    events:
    - calculation_method: simulated
      description: 'Return period 1 year(s) (source: Collection.summaries.rp).'
      disaster_identifiers: []
      hazard:
        classification: null
        id: TODO
        intensity_measure: wd:m
        process: coastal_flood
        trigger: null
        type: flood
      id: event_rp_1
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability: null
          return_period: 1.0
    - calculation_method: simulated
      description: 'Return period 100 year(s) (source: Collection.summaries.rp).'
      disaster_identifiers: []
      hazard:
        classification: null
        id: TODO
        intensity_measure: wd:m
        process: coastal_flood
        trigger: null
        type: flood
      id: event_rp_100
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability: null
          return_period: 100.0
    - calculation_method: simulated
      description: 'Return period 1000 year(s) (source: Collection.summaries.rp).'
      disaster_identifiers: []
      hazard:
        classification: null
        id: TODO
        intensity_measure: wd:m
        process: coastal_flood
        trigger: null
        type: flood
      id: event_rp_1000
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability: null
          return_period: 1000.0
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: wd:m
      process: coastal_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://spdx.org/licenses/CC-BY-4.0.html
lineage:
  description: 'Flood Maps represent the flood simulations across Europe (at 25 m
    resolution), indicating the maximum flood extent and depth, for different emission
    scenarios (including subsidence projections), storms, times and defense levels
    (if available). Spatial coverage: Europe Sources: protection levels (at NUTS2
    level) if available, RFSM-EDA Common usage: flood mapping, urban planning, emergency
    response. More Info about the dataset: User Handbook'
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
    name: "Universidad de Cantabria, Instituto de Hidr\u221A\xB0ulica Ambiental de\
      \ la Universidad de Cantabria 'IHCantabria'"
    risk_data_type:
    - hazard
    type: dataset
    url: www.ihcantabria.com
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
  name: Deltares
  url: https://deltares.nl
purpose: null
referenced_by: []
resources:
- access_url: https://storage.googleapis.com/coclico-data-public/coclico/coclico-stac/cfhp_all/collection.json
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
  title: 'STAC Collection: CoCliCo - Flood Maps [cfhp_all]'
- access_url: https://storage.googleapis.com/coclico-data-public/coclico/assets/thumbnails/cfhp_all.png
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Thumbnail
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
- access_url: https://coclico.avi.deltares.nl/geoserver/gwc/service/wmts?REQUEST=GetTile&SERVICE=WMTS&VERSION=1.0.0&LAYER=cfhp_all:lau_nuts_cfhp_all&STYLE=&TILEMATRIX=EPSG:900913:{z}&TILEMATRIXSET=EPSG:900913&FORMAT=application/vnd.mapbox-vector-tile&TILECOL={x}&TILEROW={y}
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Geoserver Parquet link
  download_url: null
  format: null
  id: resource_geoserverlink
  media_type: application/vnd.apache.parquet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Geoserver Parquet link
risk_data_type:
- hazard
schema: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
slug: rdls_hzd-coclico_cfhpall
spatial:
  bbox:
  - 1547750.0
  - 941625.0
  - 5415925.0
  - 6525950.0
  centroid: null
  countries:
  - GLO
  gazetteer_entries: []
  scale: global
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2022'
  start: '2022'
temporal_resolution: null
title: CoCliCo - Flood Maps [cfhp_all]
version: null
vulnerability: null
---
