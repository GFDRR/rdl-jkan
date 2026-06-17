---
attributions:
- entity:
    affiliation: null
    email: null
    name: Action Contre la Faim (ACF) - Regional Office West and Central Africa
    url: https://data.humdata.org/dataset/surveillance-agricole-a-tombouctou-et-youwarou-au-mali
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Action Against Hunger ACF - Regional Office for West and Central Africa ROWCA
  url: https://data.humdata.org/dataset/surveillance-agricole-a-tombouctou-et-youwarou-au-mali
creator:
  affiliation: null
  email: null
  name: Action Against Hunger ACF - Regional Office for West and Central Africa ROWCA
  url: https://data.humdata.org/dataset/surveillance-agricole-a-tombouctou-et-youwarou-au-mali
dataset_id: rdls_he-mli_acfrowca_surveillanceagricoletombo_2023
description: "Ces donn\xE9es sont accessibles librement \xE0 des fins humanitaires\
  \ ou de recherche. L'exploitation commerciale de tout ou partie de ces donn\xE9\
  es est interdite. Aucune compensation ne peut \xEAtre exig\xE9e en \xE9change de\
  \ la diffusion de ces donn\xE9es. Action Contre la Faim (ACF), International Rescue\
  \ Committee (IRC) et la Direction du D\xE9veloppement et de la Coop\xE9ration Suisse\
  \ (DDC) doivent \xEAtre mentionn\xE9s pour l'utilisation de ces donn\xE9es. Pour\
  \ plus d'informations, veuillez visiter : www.sigsahel.info These data are freely\
  \ accessible for humanitarian or research purposes. Any commercial exploitation\
  \ of this data is prohibited. No compensation can be demanded in exchange for the\
  \ dissemination of this data. Action Against Hunger (ACF), the International Rescue\
  \ Committee (IRC), and the Swiss Agency for Development and Cooperation (SDC) must\
  \ be credited for the use of this data. For more information, please visit: www.sigsahel.info.\
  \ [Source: This metadata record was automatically extracted from the Humanitarian\
  \ Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/surveillance-agricole-a-tombouctou-et-youwarou-au-mali]"
details: null
exposure:
- asset_type:
    description: Agricultural parcels under surveillance with spatial boundaries and
      crop production characteristics
    id: agriculture
    scheme: null
    title: null
    uri: null
  category: agriculture
  id: exposure_1
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: area
      unit: null
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
      intensity_measure: SPI:-
      process: agricultural_drought
      trigger: null
      type: drought
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: drought
license: CC-BY-4.0
lineage:
  description: Agricultural surveillance data collected through systematic field monitoring
    of sampled parcels in Timbuktu and Youwarou regions from July 2023 to January
    2025. Observations include crop phenology stages, rainfall and irrigation water
    availability, temperature stress, and estimated production outcomes. Spatial parcel
    boundaries are provided as shapefiles to enable geographic analysis of agricultural
    drought impacts.
  sources:
  - id: source_1
    license: null
    name: Action Contre la Faim (ACF) - Regional Office West and Central Africa
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/surveillance-agricole-a-tombouctou-et-youwarou-au-mali
  rel: source
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: Sample Survey
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Mali - Surveillance Agricole \xE0 Tombouctou et Youwarou (Donn\xE9\
    es Surveillance Agricole Tombouctou)"
  download_url: https://data.humdata.org/dataset/a92ca34c-2a28-4986-8213-95e6477e5dd6/resource/3f36d097-d150-4f41-b191-cfa0f6d1db2e/download/acf_donnees_surveillance_agricole_tombouctou_youwarou_20230711-20250131.xlsx
  format: null
  id: resource_3f36d097
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ACF_Donnees_Surveillance_Agricole_Tombouctou_Youwarou_20230711-20250131.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Informations et localisation des parcelles surveill\xE9es. Informations\
    \ and localisation of the monitored parcels."
  download_url: https://data.humdata.org/dataset/a92ca34c-2a28-4986-8213-95e6477e5dd6/resource/0c5c0e7f-a9b7-4ecf-9fa6-b030392da78f/download/acf_parcelles_surveillance_agricole_tombouctou_youwarou.xlsx
  format: null
  id: resource_0c5c0e7f
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ACF_Parcelles_Surveillance_Agricole_Tombouctou_Youwarou.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Polygones des parcelles surveill\xE9es. Polygons of the monitored\
    \ parcels."
  download_url: https://data.humdata.org/dataset/a92ca34c-2a28-4986-8213-95e6477e5dd6/resource/01549a8d-2173-46e5-86b0-a133a5cb4526/download/acf_parcelles_surveillance_agricole_tombouctou_youwarou.zip
  format: null
  id: resource_01549a8d
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ACF_Parcelles_Surveillance_Agricole_Tombouctou_Youwarou.zip
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-mli_acfrowca_surveillanceagricoletombo_2023
spatial:
  bbox: null
  centroid: null
  countries:
  - MLI
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2025-01-31'
  start: '2023-07-11'
temporal_resolution: null
title: "Mali - Surveillance Agricole \xE0 Tombouctou et Youwarou"
version: null
vulnerability: null
---
