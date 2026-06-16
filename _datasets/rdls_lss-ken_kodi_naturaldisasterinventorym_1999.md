---
attributions:
- entity:
    affiliation: null
    email: null
    name: National Disaster preparedness centre
    url: https://data.humdata.org/dataset/kenya-natural-disaster-inventory-mapped-by-event-type-1999-2013
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Kenya Open Data Initiative (inactive)
  url: https://data.humdata.org/dataset/kenya-natural-disaster-inventory-mapped-by-event-type-1999-2013
creator:
  affiliation: null
  email: null
  name: Kenya Open Data Initiative (inactive)
  url: https://data.humdata.org/dataset/kenya-natural-disaster-inventory-mapped-by-event-type-1999-2013
dataset_id: rdls_lss-ken_kodi_naturaldisasterinventorym_1999
description: 'The National Disaster inventory is a record of Natural Disasters including
  floods, thunderstorms, forest fires, mudslides and disease outbreaks etc. The inventory
  keeps track of the losses of life destruction of property and infrastructure, injury
  and displacement due to these incidents.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/kenya-natural-disaster-inventory-mapped-by-event-type-1999-2013]'
details: This dataset has been sourced automatically from the Kenya Open data initiative
  portal
exposure: []
hazard: null
license: CC0-1.0
lineage:
  description: The National Disaster Inventory is a census-based record compiled by
    Kenya's National Disaster Preparedness Centre documenting natural disaster events
    (floods, thunderstorms, forest fires, mudslides, disease outbreaks) and their
    direct impacts on populations and infrastructure. The dataset tracks losses of
    life, property destruction, injuries, and displacement across event types.
  sources:
  - id: source_1
    license: null
    name: National Disaster preparedness centre
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/kenya-natural-disaster-inventory-mapped-by-event-type-1999-2013
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by flood events
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
  - asset_category: infrastructure
    asset_dimension: structure
    description: Infrastructure destruction from flood events
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
        metric: loss
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Population affected by thunderstorm events
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_convective_storm
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: convective_storm
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
  - asset_category: natural_environment
    asset_dimension: product
    description: Forest destruction from wildfire events
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_wildfire
      intensity_measure: FWI:-
      process: null
      trigger: null
      type: wildfire
    id: loss_4
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: area
          unit: null
        metric: loss
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Population affected by mudslide events
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
    description: Population displaced by flood events
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
    id: loss_6
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: displaced
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Fatalities from flood events
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
    id: loss_7
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: casualty_count
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Injuries from flood events
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
    id: loss_8
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: ppl_injured
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
purpose: Census
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The National Disaster inventory is a record of Natural Disasters including
    floods, thunderstorms, forest fires, mudslides and disease outbreaks etc. The
    inventory keeps track of the losses of life destruction of property and infrastructure,
    injury and displacement due to these incidents.
  download_url: https://data.humdata.org/dataset/99687670-1f82-4b6b-86e6-70b6fee18734/resource/2ebef02a-72a0-4816-87b8-f295ad1f0fab/download/national_natural_disaster_inventory.csv
  format: null
  id: resource_2ebef02a
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: National_Natural_Disaster_Inventory.csv
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-ken_kodi_naturaldisasterinventorym_1999
spatial:
  bbox: null
  centroid: null
  countries:
  - KEN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2013-12-30'
  start: '1999-01-04'
temporal_resolution: null
title: Kenya - Natural Disaster Inventory Mapped by Event Type
version: null
vulnerability: null
---
