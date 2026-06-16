---
attributions:
- entity:
    affiliation: null
    email: null
    name: IOM Afghanistan Humanitarian Assistance Database (HADB)
    url: https://data.humdata.org/dataset/natural-disaster-incidents-from-1-january-to-31-december-2016
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: OCHA Field Office reports
    url: https://data.humdata.org/dataset/natural-disaster-incidents-from-1-january-to-31-december-2016
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: ANDNA
    url: https://data.humdata.org/dataset/natural-disaster-incidents-from-1-january-to-31-december-2016
  id: attribution_3
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Afghanistan
  url: https://data.humdata.org/dataset/natural-disaster-incidents-from-1-january-to-31-december-2016
creator:
  affiliation: null
  email: null
  name: OCHA Afghanistan
  url: https://data.humdata.org/dataset/natural-disaster-incidents-from-1-january-to-31-december-2016
dataset_id: rdls_lss-afg_ochaafg_naturaldisasterincidents2_2016
description: '1) Natural disaster events include avalanches,earthquake, flooding,
  heavy rainfall & snowfall, and landslides & mudflows as recorded by OCHA field offices
  and IOM Afghanistan Humanitarian Assistance Database (HADB). 2) A natural disaster
  incident is defined as an event that has affected (i.e. impacted) people, who may
  or may not require humanitarian assistance. 3) HADB information is used as a main
  reference and supplemented by OCHA Field Office reports for those incidents where
  information is not available from the HADB. OCHA information includes assessment
  figures from OCHA, ANDMA, Red Crescent Societies, national NGOs, international NGOs,
  and ERM. 4) The number of affected people and houses damaged or destroyed are based
  on the reports received. These figures may change as updates are received.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/natural-disaster-incidents-from-1-january-to-31-december-2016]'
details: These figures may fluctuate since the number of affected people, people killed
  and injured, and houses damaged or destroyed are based on a combination of verified
  and non-verified reports received. Hence, these figures may change as updates are
  received.
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: Natural disaster incident data compiled from IOM Afghanistan's Humanitarian
    Assistance Database (HADB) as the primary source, supplemented by OCHA Field Office
    reports and ANDNA assessments for incidents with incomplete HADB coverage. The
    dataset records observed hazard events (avalanches, earthquakes, flooding, heavy
    rainfall, snowfall, landslides, mudflows) that impacted populations in Afghanistan
    during 2016, capturing affected counts and fatalities per incident.
  sources:
  - id: source_1
    license: null
    name: IOM Afghanistan Humanitarian Assistance Database (HADB)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: OCHA Field Office reports
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_3
    license: null
    name: ANDNA
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/natural-disaster-incidents-from-1-january-to-31-december-2016
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by flood incidents in Afghanistan during 2016
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
        metric: exposure
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Fatalities from flood incidents in Afghanistan during 2016
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
        metric: death
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Population affected by earthquake incidents in Afghanistan during
      2016
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: null
      trigger: null
      type: earthquake
    id: loss_3
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
  - asset_category: population
    asset_dimension: population
    description: Fatalities from earthquake incidents in Afghanistan during 2016
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: null
      trigger: null
      type: earthquake
    id: loss_4
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: death
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Population affected by landslide and mudflow incidents in Afghanistan
      during 2016
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: null
      trigger: null
      type: landslide
    id: loss_5
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
  - asset_category: population
    asset_dimension: population
    description: Fatalities from landslide and mudflow incidents in Afghanistan during
      2016
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: null
      trigger: null
      type: landslide
    id: loss_6
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: death
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
  description: Natural disaster events include avalanches, earthquakes, flooding,
    heavy rainfall & snowfall, and landslides & mudflows as recorded by OCHA field
    offices and IOM Afghanistan Humanitarian Assistance Database (HADB).
  download_url: https://data.humdata.org/dataset/dd05bb07-576a-40fe-a673-b3efeea78652/resource/f52cb883-c118-43d8-b59e-811e0c7a46a7/download/afghanistan-natural-disaster-incidents-from-1-january-to-31-dec-2016.xlsx
  format: null
  id: resource_f52cb883
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: afghanistan-natural-disaster-incidents-from-1-january-to-31-dec-2016.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Natural disaster events include avalanches, earthquakes, flooding,
    heavy rainfall & snowfall, and landslides & mudflows as recorded by OCHA field
    offices and IOM Afghanistan Humanitarian Assistance Database (HADB).
  download_url: https://data.humdata.org/dataset/dd05bb07-576a-40fe-a673-b3efeea78652/resource/f48c2fd7-9f36-47eb-9db9-ce6a8c04b30a/download/afghanistan-natural-disaster-incidents-from-1-january-to-31-dec-2016.csv
  format: null
  id: resource_f48c2fd7
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: afghanistan-natural-disaster-incidents-from-1-january-to-31-dec-2016.csv
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-afg_ochaafg_naturaldisasterincidents2_2016
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
  end: '2016-10-29'
  start: '2016-01-01'
temporal_resolution: null
title: Afghanistan - Natural disaster incidents in 2016
version: null
vulnerability: null
---
