---
attributions:
- entity:
    affiliation: null
    email: null
    name: OCHA
    url: https://data.humdata.org/dataset/afghanistan-natural-disaster-incidents-in-2022
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: ANDMA
    url: https://data.humdata.org/dataset/afghanistan-natural-disaster-incidents-in-2022
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: IOM
    url: https://data.humdata.org/dataset/afghanistan-natural-disaster-incidents-in-2022
  id: attribution_3
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Red Crescent Societies
    url: https://data.humdata.org/dataset/afghanistan-natural-disaster-incidents-in-2022
  id: attribution_4
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: National and international NGOs
    url: https://data.humdata.org/dataset/afghanistan-natural-disaster-incidents-in-2022
  id: attribution_5
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: ERM
    url: https://data.humdata.org/dataset/afghanistan-natural-disaster-incidents-in-2022
  id: attribution_6
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Afghanistan
  url: https://data.humdata.org/dataset/afghanistan-natural-disaster-incidents-in-2022
creator:
  affiliation: null
  email: null
  name: OCHA Afghanistan
  url: https://data.humdata.org/dataset/afghanistan-natural-disaster-incidents-in-2022
dataset_id: rdls_el-afg_ochaafg_naturaldisasterincidents2_2022
description: '1) Natural disaster events include avalanches, earthquakes, flooding,
  heavy rainfall & snowfall, and landslides & mudflows as recorded by OCHA field offices
  based on assessments in the field. 2) A natural disaster incident is defined as
  an event that has affected (i.e. impacted) people, who may or may not require humanitarian
  assistance. 3) The information includes assessment figures from OCHA, ANDMA, IOM,
  Red Crescent Societies, national NGOs, international NGOs, and ERM. 4) The number
  of affected people and houses damaged or destroyed are based on the reports received.
  These figures may change as updates are received.. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/afghanistan-natural-disaster-incidents-in-2022]'
details: These figures may fluctuate since the number of affected population, people
  killed and injured, and houses damaged or destroyed are based on a combination of
  verified reports and information not verified by inter-agency assessments. Hence,
  these figures may change as updates are received.
exposure:
- asset_type:
    description: Houses damaged or destroyed by natural disaster incidents
    id: buildings
    scheme: null
    title: null
    uri: null
  category: buildings
  id: exposure_1
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
- asset_type:
    description: Affected population impacted by natural disaster incidents
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_2
  metrics:
  - dimension: population
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Post-event disaster incident data compiled from direct field assessments
    conducted by OCHA and humanitarian partners (ANDMA, IOM, Red Crescent Societies,
    national and international NGOs, ERM) across Afghanistan during January-September
    2022. Affected population counts and building damage figures were extracted from
    incident reports and field assessments documenting the impacts of avalanches,
    earthquakes, flooding, heavy rainfall, snowfall, and landslide/mudflow events.
  sources:
  - id: source_1
    license: null
    name: OCHA
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: ANDMA
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_3
    license: null
    name: IOM
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_4
    license: null
    name: Red Crescent Societies
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_5
    license: null
    name: National and international NGOs
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_6
    license: null
    name: ERM
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/afghanistan-natural-disaster-incidents-in-2022
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from flooding incidents
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: loss
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Affected population from flooding incidents
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
    id: loss_2
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
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from landslide and mudflow incidents
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: null
      trigger: null
      type: landslide
    id: loss_3
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: loss
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Affected population from landslide and mudflow incidents
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: null
      trigger: null
      type: landslide
    id: loss_4
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
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from earthquake incidents
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: null
      trigger: null
      type: earthquake
    id: loss_5
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: loss
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Affected population from earthquake incidents
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: null
      trigger: null
      type: earthquake
    id: loss_6
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
purpose: Direct Observational Data/Anecdotal Data
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Natural disaster events include avalanches, earthquakes, flooding,
    heavy rainfall & snowfall, and landslides & mudflows as recorded by OCHA field
    offices based on assessments in the field.
  download_url: https://data.humdata.org/dataset/a293d673-e15a-4f14-a311-01fdfd83d7bd/resource/fbc6b7b0-2eb0-46ab-a6e4-f67ed02c939e/download/afghanistan-natural-disaster-incidents-from-january-to-september-2022.xlsx
  format: null
  id: resource_fbc6b7b0
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: afghanistan-natural-disaster-incidents-from-january-to-september-2022.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Natural disaster events include avalanches, earthquakes, flooding,
    heavy rainfall & snowfall, and landslides & mudflows as recorded by OCHA field
    offices based on assessments in the field.
  download_url: https://data.humdata.org/dataset/a293d673-e15a-4f14-a311-01fdfd83d7bd/resource/f71e86a5-1041-49f8-80ff-53ebb3cc59fc/download/afghanistan-natural-disaster-incidents-from-january-to-september-2022.csv
  format: null
  id: resource_f71e86a5
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: afghanistan-natural-disaster-incidents-from-january-to-september-2022.csv
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-afg_ochaafg_naturaldisasterincidents2_2022
spatial:
  bbox: null
  centroid: null
  countries:
  - AFG
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2022-09-19'
  start: '2022-01-01'
temporal_resolution: null
title: Afghanistan - Natural Disaster Incidents in 2022
version: null
vulnerability: null
---
