---
attributions:
- entity:
    affiliation: null
    email: null
    name: Copernicus WISC project
    url: https://data.humdata.org/dataset/climada-storm-europe-dataset
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: ERA5 reanalysis
    url: https://data.humdata.org/dataset/climada-storm-europe-dataset
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: CMIP6 climate models
    url: https://data.humdata.org/dataset/climada-storm-europe-dataset
  id: attribution_3
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: CLIMADA
    url: https://data.humdata.org/dataset/climada-storm-europe-dataset
  id: attribution_4
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: "ETH Z\xFCrich - Weather and Climate Risks"
  url: https://data.humdata.org/dataset/climada-storm-europe-dataset
creator:
  affiliation: null
  email: null
  name: "ETH Z\xFCrich - Weather and Climate Risks"
  url: https://data.humdata.org/dataset/climada-storm-europe-dataset
dataset_id: rdls_hzd-ukr_ethzurich_stormeuropedatadisasterri_1940
description: "European winter storm [gust in meters per second] footprints for Ukraine.\
  \ Data presented here is historical, observed data based on the Copernicus WISC\
  \ project event footprints 1940-2014. Further modelled data are available from the\
  \ CLIMADA Data API these include 50 probabilistic events per original event, at\
  \ 4 kilometers resolution. Data available for European countries, and corresponds\
  \ to the storm hazard today. See key reference R\xF6\xF6sli et al. 2021. 2. Winter\
  \ storm hazards generated from ERA5 (1980-2010) and CMIP6 models (1980-2010 and\
  \ 2070-2100). In that second case, only Europe wide datasets are available, with\
  \ lower resolution (depending on the GCM or ERA5 model). See Severino et al. 2023..\
  \ [Source: This metadata record was automatically extracted from the Humanitarian\
  \ Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/climada-storm-europe-dataset]"
details: '2024-01-15: Only Ukraine data since other HRP countries are not in the source'
exposure: []
hazard:
  event_sets:
  - analysis_type: probabilistic
    calculation_method: simulated
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: sws_10m:m/s
      process: extratropical_cyclone
      trigger: null
      type: strong_wind
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: strong_wind
license: CC-BY-4.0
lineage:
  description: Historical winter storm footprints from the Copernicus WISC project
    (1940-2014) were used as baseline events. Wind speed fields were generated from
    ERA5 reanalysis (1980-2010) and CMIP6 climate model outputs (1980-2010 and 2070-2100)
    at 4 km resolution. The CLIMADA platform generated 50 probabilistic synthetic
    events per historical event to create a comprehensive probabilistic windstorm
    hazard dataset for Ukraine and Europe, enabling disaster risk assessment under
    current and future climate conditions.
  sources:
  - id: source_1
    license: null
    name: Copernicus WISC project
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: ERA5 reanalysis
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_3
    license: null
    name: CMIP6 climate models
    risk_data_type:
    - hazard
    type: model
    url: null
    used_in: hazard
  - id: source_4
    license: null
    name: CLIMADA
    risk_data_type:
    - hazard
    type: model
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/climada-storm-europe-dataset
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
  url: https://www.nat-hazards-earth-syst-sci-discuss.net/nhess-2020-115
- author_names: null
  date_published: null
  doi: null
  id: reference_2
  name: Methodology documentation
  url: http://dx.doi.org/10.1002/met.2035
- author_names: null
  date_published: null
  doi: null
  id: reference_3
  name: Methodology documentation
  url: https://doi.org/10.5194/egusphere-2023-205
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: European winter storm gust wind speeds over the period 1940-2013 at
    admin1 level for Ukraine
  download_url: https://data.humdata.org/dataset/2b6d2fcf-25ad-4783-9653-8a20cfb80b43/resource/d79cc454-2c5d-4f9c-bfd5-67760403e5a9/download/admin1-summaries-storm-europe.csv
  format: null
  id: resource_d79cc454
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: admin1-summaries-storm-europe.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: European winter storm gust wind speeds by admin1 or admin2 for each
    storm for Ukraine
  download_url: https://data.humdata.org/dataset/2b6d2fcf-25ad-4783-9653-8a20cfb80b43/resource/11cfc323-c4fa-4619-9562-ae63db9b94e3/download/admin1-timeseries-summaries-storm-europe.csv
  format: null
  id: resource_11cfc323
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: admin1-timeseries-summaries-storm-europe.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Gridded (4kmx4km) European winter storm gust wind speeds for Ukraine
    at with admin1 name column
  download_url: https://data.humdata.org/dataset/2b6d2fcf-25ad-4783-9653-8a20cfb80b43/resource/204edb57-68b1-4d04-bfc6-c842f3f00e9d/download/ukraine-admin1-storm-europe.csv
  format: null
  id: resource_204edb57
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ukraine-admin1-storm-europe.csv
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-ukr_ethzurich_stormeuropedatadisasterri_1940
spatial:
  bbox: null
  centroid: null
  countries:
  - UKR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2013-12-05'
  start: '1940-11-01'
temporal_resolution: null
title: 'Storm Europe: Data for Disaster Risk Assessment (Ukraine Only)'
version: null
vulnerability: null
---
