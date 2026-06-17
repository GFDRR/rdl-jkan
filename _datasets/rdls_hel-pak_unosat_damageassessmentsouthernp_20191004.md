---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/damage-assessment-in-the-southern-part-of-new-mirpur-azad-jammu-and-kashmir-pakistan-as-of
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-in-the-southern-part-of-new-mirpur-azad-jammu-and-kashmir-pakistan-as-of
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-in-the-southern-part-of-new-mirpur-azad-jammu-and-kashmir-pakistan-as-of
dataset_id: rdls_hel-pak_unosat_damageassessmentsouthernp_20191004
description: 'UNOSAT code: EQ20190924PAK This map illustrates satellite based structure
  damage assessment in the southern part of New Mirpur City, Azad Kashmir, Pakistan
  that was affected by the 5.6 magnitude Mirpur earthquake of the 24th of September
  2019 with an epicenter SE of New Mipur City. UNITAR-UNOSAT has identified within
  the extent of this map 31 potentially damaged structures South of New Mirpur City.
  This is a preliminary analysis and has not yet been validated in the field. Please
  send ground feedback to UNITAR - UNOSAT.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/damage-assessment-in-the-southern-part-of-new-mirpur-azad-jammu-and-kashmir-pakistan-as-of]'
details: This is a preliminary assessment and has not yet been validated in the field.
  It is important to consider the characteristics of the source imagery used in the
  analyses when interpreting results. For damage assessments it should be noted that
  only significant damage to the structural integrity of the buildings analyzed can
  be seen in imagery, while minor damage such as cracks or holes may not be visible
  at all. For flood extractions using radar data it is important to note that urban
  areas and highly vegetated areas may mask the flood signature and result in underestimation
  of flood waters. Users with specific questions or concerns should contact unosat@unitar.org
  to seek clarification.
exposure:
- asset_type:
    description: Building structures in southern New Mirpur City identified through
      satellite imagery analysis
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
      intensity_measure: PGA:g
      process: ground_motion
      trigger: null
      type: earthquake
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: earthquake
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT analysts compared pre- and post-event satellite imagery of southern
    New Mirpur City to identify structural changes and damage patterns resulting from
    the 24 September 2019 magnitude 5.6 earthquake. Satellite-detected potentially
    damaged structures were mapped and attributed with confidence levels and damage
    classifications to produce a preliminary damage assessment dataset.
  sources:
  - id: source_1
    license: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/damage-assessment-in-the-southern-part-of-new-mirpur-azad-jammu-and-kashmir-pakistan-as-of
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from 5.6 magnitude earthquake assessed via
      satellite imagery (31 potentially damaged structures identified)
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
  description: Damage assessment in the Southern part of New Mirpur, Azad Jammu and
    Kashmir, Pakistan, as of 02 October 2019 (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/PK/EQ20190924PAK/EQ20190924PAK_gdb.zip
  format: Geodatabase
  id: resource_a06950ce
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EQ20190924PAK_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Damage assessment in the Southern part of New Mirpur, Azad Jammu and
    Kashmir, Pakistan, as of 02 October 2019 (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/PK/EQ20190924PAK/EQ20190924PAK_SHP.zip
  format: null
  id: resource_9d387c35
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EQ20190924PAK_SHP.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-pak_unosat_damageassessmentsouthernp_20191004
spatial:
  bbox: null
  centroid: null
  countries:
  - PAK
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2019-10-04'
temporal_resolution: null
title: Damage assessment in the Southern part of New Mirpur, Azad Jammu and Kashmir,
  Pakistan, as of 02 October 2019
version: null
vulnerability: null
---
