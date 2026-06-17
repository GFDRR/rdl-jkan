---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-pico-de-fogo-volcanic-eruption-fogo-island-cape-verde-impact-november-28-2014
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-pico-de-fogo-volcanic-eruption-fogo-island-cape-verde-impact-november-28-2014
dataset_id: rdls_hel-cpv_unosat_geodatapicodefogovolcanic_20141128
description: 'This map illustrates areas affected by Pico de Fogo volcano as seen
  in a WorldView-2 image acquired 25 November 2014 and LANDSAT-8 data acquired the
  24 of November. The lava flow is continuing from the subsidiary vent located in
  the western flank of the Pico de Fogo Mountain and magma and the lava reached the
  areas close to Portela, Cha Das Caldeiras and Bangaeira villages. About 3400 meters
  of the main road and 4600 m of secondary roads and paths in the caldera are affected
  and are potentially out of use (i.e. 8000 m of roadways potentially affected). The
  inset of this map illustrates the incandescent lava and smoke as seen with false
  colors as captured by WorldView-2 satellite. ~150 ha of lava could be observed on
  the 24 November 2014 and ~260 ha the on 25 November 2014. Note that the lava flow
  is likely underestimated because of smoke especially in the areas close to the vent.
  This analysis has not yet been validated in the field. Please send ground feedback
  to UNITAR /UNOSAT.. [Source: This metadata record was automatically extracted from
  the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/geodata-of-pico-de-fogo-volcanic-eruption-fogo-island-cape-verde-impact-november-28-2014]'
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
    description: Road network affected by lava flow in the caldera, including main
      and secondary roads
    id: infrastructure
    scheme: null
    title: null
    uri: null
  category: infrastructure
  id: exposure_1
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: length
      unit: null
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
      intensity_measure: h_vaf:mm
      process: lava
      trigger: null
      type: volcanic
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: volcanic
license: CC-BY-4.0
lineage:
  description: UNOSAT analysts compared multi-temporal satellite imagery (WorldView-2
    acquired 25 November 2014 and LANDSAT-8 acquired 24 November 2014) to delineate
    lava flow extent and identify affected roadways in the Fogo Island caldera. The
    resulting geodata product maps the observed volcanic hazard footprint and quantifies
    direct infrastructure impacts.
  sources:
  - id: source_1
    license: null
    name: United Nations Satellite Centre (UNOSAT)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/geodata-of-pico-de-fogo-volcanic-eruption-fogo-island-cape-verde-impact-november-28-2014
  rel: source
loss:
  losses:
  - asset_category: infrastructure
    asset_dimension: structure
    description: Direct infrastructure damage from lava flow affecting approximately
      8000 meters of roadways
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_volcanic
      intensity_measure: h_vaf:mm
      process: null
      trigger: null
      type: volcanic
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
  description: Cabo Verde - Geodata of Pico de Fogo Volcanic Eruption, Fogo Island,
    Cape Verde - Impact (KML)
  download_url: https://cern.ch/unosat-maps/CV/VO20141124CPV/WV20141125_lava_Flow_Fogo.kmz
  format: null
  id: resource_084ed999
  media_type: application/vnd.google-earth.kml+xml
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: WV20141125_lava_Flow_Fogo.kmz
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-cpv_unosat_geodatapicodefogovolcanic_20141128
spatial:
  bbox: null
  centroid: null
  countries:
  - CPV
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2014-11-28'
temporal_resolution: null
title: Cabo Verde - Geodata of Pico de Fogo Volcanic Eruption, Fogo Island, Cape Verde
  - Impact
version: null
vulnerability: null
---
