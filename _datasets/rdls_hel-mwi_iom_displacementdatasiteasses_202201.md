---
attributions:
- entity:
    affiliation: null
    email: null
    name: United Nations Satellite Centre (UNOSAT)
    url: https://data.humdata.org/dataset/malawi-displacement-data-site-assessment-tropical-storm-ana-iom-dtm
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: International Organization for Migration (IOM) DTM
    url: https://data.humdata.org/dataset/malawi-displacement-data-site-assessment-tropical-storm-ana-iom-dtm
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/malawi-displacement-data-site-assessment-tropical-storm-ana-iom-dtm
creator:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/malawi-displacement-data-site-assessment-tropical-storm-ana-iom-dtm
dataset_id: rdls_hel-mwi_iom_displacementdatasiteasses_202201
description: 'Following the passage of tropical storm Ana across southern Malawi,
  the districts of Chikwawa, Mulanje, Nsanje and Phalombe have been severely hit by
  torrential and persistent rains, although there are reports of other districts also
  been affected by the onset, such as Mulanje, Chiradzulu and Neno. Situational overviews
  conducted by the United Nations Satellite Centre (UNOSAT) reported a flooded area
  of 20Km2 in the districts of Balaka, Blantyre, Neno and Zomba, where 5,400 people
  are potentially exposed or living close to flooded areas. Also, the Malawian government
  agency of Department of Disaster Management Affairs (DoDMA) reported several blocked
  roads in the Phalombe district, which negatively affects the daily lives of several
  households whom are relegated to camps and obstructing their access to essential
  services, such as health facilities.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/malawi-displacement-data-site-assessment-tropical-storm-ana-iom-dtm]'
details: null
exposure:
- asset_type:
    description: Population potentially exposed or living close to flooded areas
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_1
  metrics:
  - dimension: population
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
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
      intensity_measure: AA:km2
      process: pluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: "UNOSAT conducted satellite-based situational overviews to map flood\
    \ extent (20 km\xB2) across Balaka, Blantyre, Neno and Zomba districts following\
    \ tropical storm Ana. IOM DTM applied site assessment methodology to identify\
    \ 5,400 people potentially exposed or living in flooded areas, integrating satellite\
    \ hazard data with ground-based displacement and exposure surveys."
  sources:
  - id: source_1
    license: null
    name: United Nations Satellite Centre (UNOSAT)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: International Organization for Migration (IOM) DTM
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/malawi-displacement-data-site-assessment-tropical-storm-ana-iom-dtm
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by tropical storm Ana flooding in Malawi
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: AA:km2
      process: null
      trigger: null
      type: flood
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: exposure
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: null
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Throughout an existing network of enumerators on site, IOM's Displacement
    Tracking Matrix (DTM) teams in Malawi are providing both logistical and technical
    support in developing rapid assessments in 131 sites from 22 Traditional Areas
    within the Districts of Chikwawa, Mulanje, Nsanje and Phalombe. The results of
    this initial assessment are based on key informant interviews with local stakeholders
    at District level as well as site assessments in key locations from 28th to 31st
    January. The results of this rapid assessment are indicative of the current situation
    on the ground but have yet to be validated extensively in the field.
  download_url: https://data.humdata.org/dataset/20c83e93-b225-4132-af68-42de799d4bd0/resource/969f3105-dd01-449c-a5e1-28a3ac6fed98/download/hdx_dtm_malawi_baseline_assessment_tc_ana_round1.xlsx
  format: null
  id: resource_969f3105
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Malawi - BA Tropical Storm Ana - R1
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-mwi_iom_displacementdatasiteasses_202201
spatial:
  bbox: null
  centroid: null
  countries:
  - MWI
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2022-01-31'
  start: '2022-01-28'
temporal_resolution: null
title: Malawi Displacement Data - Site Assessment - Tropical Storm Ana - [IOM DTM]
version: null
vulnerability: null
---
