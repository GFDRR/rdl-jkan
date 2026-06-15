---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-muisne-esmeraldas-province-ecuador-april-22-2016
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-muisne-esmeraldas-province-ecuador-april-22-2016
dataset_id: rdls_lss-ecu_unosat_geodatadamageassessmentmu_20160422
description: "This map illustrates satellite-detected, potential damaged structures\
  \ in Muisne, Esmeraldas Province, Ecuador. The analyzed area is located approximately\
  \ 30 km north of the 16 April 2016 Muisne earthquake mainshock epicenter. This analysis\
  \ is carried out using Pl\xE9iades satellite image acquired 20 April 2016 and a\
  \ WorldView-3 image acquired 12 March 2016. UNITAR-UNOSAT identified 450 potentially\
  \ damaged structures of which 139 are destroyed, 206 severely damaged, and 105 moderately\
  \ damaged. This is a preliminary analysis and not yet been validated in the field.\
  \ Please send ground feedback to UNITAR-UNOSAT.. [Source: This metadata record was\
  \ automatically extracted from the Humanitarian Data Exchange (HDX); Original dataset:\
  \ https://data.humdata.org/dataset/geodata-of-damage-assessment-of-muisne-esmeraldas-province-ecuador-april-22-2016]"
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
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: "UNOSAT analysts compared pre-event (12 March 2016 WorldView-3) and\
    \ post-event (20 April 2016 Pl\xE9iades) satellite imagery of Muisne to detect\
    \ structural damage from the 16 April 2016 earthquake. Visual interpretation identified\
    \ 450 damaged structures classified into three severity categories (destroyed,\
    \ severely damaged, moderately damaged) through change detection analysis."
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
- href: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-muisne-esmeraldas-province-ecuador-april-22-2016
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from the 16 April 2016 Muisne earthquake assessed
      via satellite imagery
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
  description: Geodata of Damage Assessment of Muisne, Esmeraldas Province, Ecuador
    (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/EC/EQ20160417ECU/EQ20160417ECU_shp.zip
  format: null
  id: resource_f03d0f6f
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
  description: Geodata of Damage Assessment of Muisne, Esmeraldas Province, Ecuador
    (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/EC/EQ20160417ECU/EQ20160417ECU.gdb.zip
  format: null
  id: resource_a29e5913
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
slug: rdls_lss-ecu_unosat_geodatadamageassessmentmu_20160422
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
  start: '2016-04-22'
temporal_resolution: null
title: Geodata of Damage Assessment of Muisne, Esmeraldas Province, Ecuador
version: null
vulnerability: null
---
