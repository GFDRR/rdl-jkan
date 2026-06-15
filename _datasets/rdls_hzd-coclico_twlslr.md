---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: null
  name: "Universidad de Cantabria, Instituto de Hidr\uCE58ulica Ambiental de la Universidad\
    \ de Cantabria 'IHCantabria'"
  url: www.ihcantabria.com
creator:
  affiliation: null
  email: null
  name: "Universidad de Cantabria, Instituto de Hidr\uCE58ulica Ambiental de la Universidad\
    \ de Cantabria 'IHCantabria'"
  url: www.ihcantabria.com
dataset_id: rdls_hzd-coclico_twlslr
description: 'Future Total Water Levels (TWL) represents the combination of storm
  surge level, wave setup, tidal range and Sea Level Rise (inc. subsidence). It provides
  an indication of the maximum water levels expected at different times for different
  storms and emission scenarios. Spatial coverage: European coastline at coastal target
  points. Sources: Observational records, climate models, Copernicus Marine Service,
  Sea Level Rise projections Common usage: Coastal flood risk assessment (boundary
  conditions), infrastructure design, emergency planning. More info about the dataset:
  User Handbook. Variants in the source dataset - rp: 1.0 (1 year), 100.0 (100 years),
  1000.0 (1000 years) - Frequency at which an extreme event of total water level (related
  to storms) is expected to occur on average; scenarios: High_End (High End), None
  (No Scenario), SSP126 (SSP1-2.6), SSP245 (SSP2-4.5), SSP585 (SSP5-8.5) - Climate
  scenarios based on IPCC''s Shared Socioeconomic Pathways (SSPs). High-end (if applicable)
  refers to P83 of SSP5-8.5, taking into account low-confidence processes. Other scenarios
  use the P50; time: 2010.0, 2030.0, 2050.0, 2100.0 - Time slice applied to the data.
  Either present-day (2010) or future state representing medium (2030 till 2050) and
  long term (2050 till 2100) outlook; lon: -18.168, 34.5992 - longitude; lat: 27.6298,
  71.1914 - latitude. [Source: This metadata record was automatically extracted from
  the STAC catalog coclico (https://www.openearth.nl/coclico-workbench/data_catalog/)]'
details: null
exposure: []
hazard:
  event_sets_by_hazard_type:
    flood:
    - analysis_type: probabilistic
      calculation_method: simulated
      event_count: 3
      events:
      - calculation_method: simulated
        description: 'Return period 1 year(s) (source: Collection.summaries.rp).'
        disaster_identifiers: []
        hazard:
          classification: null
          id: hazard_flood
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
          id: hazard_flood
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
          id: hazard_flood
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
  event_sets_count: 1
license: https://spdx.org/licenses/CC-BY-4.0.html
lineage:
  description: 'Future Total Water Levels (TWL) represents the combination of storm
    surge level, wave setup, tidal range and Sea Level Rise (inc. subsidence). It
    provides an indication of the maximum water levels expected at different times
    for different storms and emission scenarios. Spatial coverage: European coastline
    at coastal target points. Sources: Observational records, climate models, Copernicus
    Marine Service, Sea Level Rise projections Common usage: Coastal flood risk assessment
    (boundary conditions), infrastructure design, emergency planning. More info about
    the dataset: User Handbook'
  sources:
  - id: source_1
    license: null
    name: "Universidad de Cantabria, Instituto de Hidr\uCE58ulica Ambiental de la\
      \ Universidad de Cantabria 'IHCantabria'"
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
  name: "Universidad de Cantabria, Instituto de Hidr\uCE58ulica Ambiental de la Universidad\
    \ de Cantabria 'IHCantabria'"
  url: www.ihcantabria.com
purpose: null
referenced_by: []
resources:
- access_url: https://storage.googleapis.com/coclico-data-public/coclico/coclico-stac/twl_SLR/collection.json
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
  title: 'STAC Collection: CoCliCo - Future Total Water Levels [twl_SLR]'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The root of the EU Coastal Target Points - TWL Return Periods combined
    with sea level rise and subsidence zarr dataset on public Google Cloud Storage.
  download_url: https://storage.googleapis.com/coclico-data-public/coclico/twl_SLR.zarr
  format: null
  id: resource_data
  media_type: application/vnd.zarr
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EU Coastal Target Points - TWL Return Periods combined with sea level rise
    and subsidence zarr root
- access_url: https://storage.googleapis.com/download/storage/v1/b/coclico-data-public/o/coclico%2Fassets%2Fthumbnails%2Ftwl_SLR.png?alt=media
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: CoCliCo - Future Total Water Levels
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
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-coclico_twlslr
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
temporal: null
temporal_resolution: null
title: CoCliCo - Future Total Water Levels
version: null
vulnerability: null
---
