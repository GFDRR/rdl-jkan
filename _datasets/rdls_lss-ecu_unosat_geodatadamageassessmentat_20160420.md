---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-atacames-area-esmeraldas-province-ecuador-april-20-2016
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-atacames-area-esmeraldas-province-ecuador-april-20-2016
dataset_id: rdls_lss-ecu_unosat_geodatadamageassessmentat_20160420
description: "This map illustrates satellite-detected potential damaged structures\
  \ in the city of Atacames in Esmeraldas Province, Ecuador, approximately 55 km north\
  \ the 16 April 2016 Muisne earthquake mainshock epicenter. Using a Pl\xE9iades satellite\
  \ image acquired 18 April 2016 and a WorldView-2 image acquired 18 August 2013,\
  \ UNITAR - UNOSAT identified 58 potentially damaged structures of which 11 were\
  \ destroyed, 14 severely damaged, and 33 moderately damaged. This is a preliminary\
  \ analysis and not yet been validated in the field. Please send ground feedback\
  \ to UNITAR - UNOSAT.. [Source: This metadata record was automatically extracted\
  \ from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-atacames-area-esmeraldas-province-ecuador-april-20-2016]"
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
license: CC-BY-4.0
lineage:
  description: "UNOSAT analysts compared pre-event (WorldView-2, 18 August 2013) and\
    \ post-event (Pl\xE9iades, 18 April 2016) satellite imagery of Atacames to detect\
    \ structural damage from the 16 April 2016 Muisne earthquake. Visual interpretation\
    \ identified 58 potentially damaged buildings classified by severity (destroyed,\
    \ severely damaged, moderately damaged). This is a preliminary remote-sensing-based\
    \ assessment not yet validated through field surveys."
  sources:
  - id: source_1
    license: null
    name: United Nations Satellite Centre (UNOSAT)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-atacames-area-esmeraldas-province-ecuador-april-20-2016
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from the 16 April 2016 Muisne earthquake assessed
      via satellite imagery comparison
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: null
      trigger: null
      type: earthquake
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
  description: Geodata of Damage Assessment of Atacames area, Esmeraldas Province,
    Ecuador (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/EC/EQ20160417ECU/EQ20160417ECU_shp.zip
  format: null
  id: resource_e8e6d2cd
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EQ20160417ECU_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Geodata of Damage Assessment of Atacames area, Esmeraldas Province,
    Ecuador (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/EC/EQ20160417ECU/EQ20160417ECU.gdb.zip
  format: null
  id: resource_d2f64c9c
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EQ20160417ECU.gdb.zip
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-ecu_unosat_geodatadamageassessmentat_20160420
spatial:
  bbox: null
  centroid: null
  countries:
  - ECU
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2016-04-20'
temporal_resolution: null
title: Geodata of Damage Assessment of Atacames area, Esmeraldas Province, Ecuador
version: null
vulnerability: null
---
