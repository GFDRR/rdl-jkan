---
attributions:
- entity:
    affiliation: null
    email: null
    name: OpenStreetMap
    url: https://data.humdata.org/dataset/damage-assessment-in-luganville-municipality-sanma-province-vanuatu
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-in-luganville-municipality-sanma-province-vanuatu
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-in-luganville-municipality-sanma-province-vanuatu
dataset_id: rdls_lss-vut_unosat_damageassessmentluganvill_20200409
description: 'UNOSAT code: TC20200403VUT This map illustrates potentially damaged
  structures and buildings in Luganville Municipality, Sanma Province, Vanuatu as
  detected by satellite image acquired after landfall of the Tropical Cyclone Harold-20
  on 6 April 2020. UNITAR-UNOSAT analysis used a Pleiades image acquired on 7 April
  2020 as post event image. Within the Luganville Municipality boundary, UNITAR-UNOSAT
  identified in the cloud free zones 1,972 potentially damaged structures. Taking
  into account the pre-building footprints provided by OpenStreetMap, this represents
  about 35 % of the total number of structures within the analyzed cloud free areas.
  This is a preliminary analysis and has not yet been validated in the field. Please
  send ground feedback to UNITAR-UNOSAT.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/damage-assessment-in-luganville-municipality-sanma-province-vanuatu]'
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
hazard: null
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts compared Pleiades satellite imagery acquired on 7 April
    2020 (post-Tropical Cyclone Harold landfall on 6 April 2020) against pre-event
    building footprints from OpenStreetMap to identify structural damage. Within cloud-free
    zones of Luganville Municipality, 1,972 potentially damaged structures were detected,
    representing approximately 35% of the building stock.
  sources:
  - id: source_1
    license: null
    name: United Nations Satellite Centre (UNOSAT)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: OpenStreetMap
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/damage-assessment-in-luganville-municipality-sanma-province-vanuatu
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from Tropical Cyclone Harold detected via
      satellite imagery
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
  description: Damage Assessment in Luganville Municipality, Sanma Province, Vanuatu
    (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/VU/TC20200403VUT/TC20200403VUT_gdb.zip
  format: Geodatabase
  id: resource_4cd8a11e
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
  description: Damage Assessment in Luganville Municipality, Sanma Province, Vanuatu
    (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/VU/TC20200403VUT/TC20200403VUT_SHP.zip
  format: null
  id: resource_a19c4e60
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20200403VUT_SHP.zip
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-vut_unosat_damageassessmentluganvill_20200409
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
  start: '2020-04-09'
temporal_resolution: null
title: Damage Assessment in Luganville Municipality, Sanma Province, Vanuatu
version: null
vulnerability: null
---
