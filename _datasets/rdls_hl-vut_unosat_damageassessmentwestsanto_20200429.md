---
attributions:
- entity:
    affiliation: null
    email: null
    name: Humanitarian OpenStreetMap
    url: https://data.humdata.org/dataset/damage-assessment-in-west-santo-and-south-santo-municipality-sanma-province-vanuatu
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldView-2 satellite imagery
    url: https://data.humdata.org/dataset/damage-assessment-in-west-santo-and-south-santo-municipality-sanma-province-vanuatu
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Pleiades satellite imagery
    url: https://data.humdata.org/dataset/damage-assessment-in-west-santo-and-south-santo-municipality-sanma-province-vanuatu
  id: attribution_3
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-in-west-santo-and-south-santo-municipality-sanma-province-vanuatu
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-in-west-santo-and-south-santo-municipality-sanma-province-vanuatu
dataset_id: rdls_hl-vut_unosat_damageassessmentwestsanto_20200429
description: 'UNOSAT code: TC20200403VUT This map illustrates potentially damaged
  structures and buildings in West Santo and South Santo Municipality, Sanma Province,
  Vanuatu as detected using WorldView-2 satellite images acquired on 17 and 19 April
  2020 and a Pleiades satellite image acquired on 27 April 2020. Within the analyzed
  zone, UNITAR-UNOSAT identified in the cloud-free zones about 3,650 potentially damaged
  structures. Taking into account the pre-building footprints provided by Humanitarian
  OpenStreetMap, this represents about 63 % of the total number of structures within
  the analyzed cloud-free areas. This is a preliminary analysis and has not yet been
  validated in the field. Please send ground feedback to UNITAR-UNOSAT.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/damage-assessment-in-west-santo-and-south-santo-municipality-sanma-province-vanuatu]'
details: This is a preliminary assessment and has not yet been validated in the field.
  It is important to consider the characteristics of the source imagery used in the
  analyses when interpreting results. For damage assessments it should be noted that
  only significant damage to the structural integrity of the buildings analyzed can
  be seen in imagery, while minor damage such as cracks or holes may not be visible
  at all. For flood extractions using radar data it is important to note that urban
  areas and highly vegetated areas may mask the flood signature and result in underestimation
  of flood waters. Users with specific questions or concerns should contact unosat@unitar.org
  to seek clarification.
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
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT analysts performed post-event damage assessment by comparing
    pre-event building footprints from Humanitarian OpenStreetMap with multi-temporal
    satellite imagery (WorldView-2 and Pleiades) acquired in April 2020 following
    Tropical Cyclone Harold. Visual interpretation of cloud-free zones identified
    approximately 3,650 potentially damaged structures, representing 63% of total
    structures in the study area.
  sources:
  - id: source_1
    license: null
    name: Humanitarian OpenStreetMap
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: WorldView-2 satellite imagery
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_3
    license: null
    name: Pleiades satellite imagery
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/damage-assessment-in-west-santo-and-south-santo-municipality-sanma-province-vanuatu
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from tropical cyclone detected via satellite
      image analysis
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: loss
        modelling: simulated
        type: direct
      loss_approach: analytical
      loss_frequency_type: probabilistic
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
  description: Damage Assessment in West Santo and South Santo Municipality, Sanma
    Province, Vanuatu (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/VU/TC20200403VUT/TC20200403VUT_gdb.zip
  format: Geodatabase
  id: resource_6ff22274
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20200403VUT_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Damage Assessment in West Santo and South Santo Municipality, Sanma
    Province, Vanuatu (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/VU/TC20200403VUT/TC20200403VUT_SHP.zip
  format: null
  id: resource_00bc8766
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20200403VUT_SHP.zip
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-vut_unosat_damageassessmentwestsanto_20200429
spatial:
  bbox: null
  centroid: null
  countries:
  - VUT
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2020-04-29'
temporal_resolution: null
title: Damage Assessment in West Santo and South Santo Municipality, Sanma Province,
  Vanuatu
version: null
vulnerability: null
---
