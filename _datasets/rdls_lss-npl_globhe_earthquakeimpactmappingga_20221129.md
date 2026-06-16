---
attributions:
- entity:
    affiliation: null
    email: null
    name: GLOBHE Crowddroner
    url: https://data.humdata.org/dataset/earthquake-mapping-from-drones-in-gairagaun-pubichauki-rural-municipality-ward-3-doti-nepal
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Globhe Drones
  url: https://data.humdata.org/dataset/earthquake-mapping-from-drones-in-gairagaun-pubichauki-rural-municipality-ward-3-doti-nepal
creator:
  affiliation: null
  email: null
  name: Globhe Drones
  url: https://data.humdata.org/dataset/earthquake-mapping-from-drones-in-gairagaun-pubichauki-rural-municipality-ward-3-doti-nepal
dataset_id: rdls_lss-npl_globhe_earthquakeimpactmappingga_20221129
description: 'Earthquake impacts mapping from drone data in Nepal (Gairagaun, Pubichauki
  rural municipality ward-3, Doti) from GLOBHE Crowddroner. The dataset includes high-resolution
  actionable drone data showing the area impacted from the earthquakes of early November
  2022. Reference: https://reliefweb.int/disaster/eq-2022-000358-npl MORE CROWDDRONING
  BY GLOBHE Web: https://globhe.com/ Facebook: https://www.facebook.com/Crowddroning
  Twitter: https://twitter.com/globhedrones Instagram: https://www.instagram.com/globhedrones/
  LinkedIn: https://www.linkedin.com/company/globhedrones/. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/earthquake-mapping-from-drones-in-gairagaun-pubichauki-rural-municipality-ward-3-doti-nepal]'
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: High-resolution drone imagery was collected by GLOBHE Crowddroner over
    the earthquake-impacted area in Gairagaun, Pubichauki rural municipality ward-3,
    Doti, Nepal following the November 2022 earthquake events. The drone data was
    processed into an orthomosaic (georeferenced aerial image) enabling visual assessment
    and mapping of building damage and earthquake impacts on the ground.
  sources:
  - id: source_1
    license: null
    name: GLOBHE Crowddroner
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/earthquake-mapping-from-drones-in-gairagaun-pubichauki-rural-municipality-ward-3-doti-nepal
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage assessment from November 2022 earthquake in
      Doti district
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
purpose: Direct Observational Data/Anecdotal Data
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'High-resolution orthomosaic, showing the area impacted from the earthquake
    happened on early November 2022. Area: 45.7 hectares Spatial resolution: 3.1 cm/px'
  download_url: https://data.humdata.org/dataset/957ec564-8075-460d-aa65-6222480c76e3/resource/3934fea3-c7d4-4004-810f-fba01c61b0a5/download/gairagaun-most-affectedarea_orthomosaic.tif
  format: null
  id: resource_3934fea3
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Gairagaun_Nepal_Orthomosaic_GLOBHE.tif
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-npl_globhe_earthquakeimpactmappingga_20221129
spatial:
  bbox: null
  centroid: null
  countries:
  - NPL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2022-11-29'
temporal_resolution: null
title: Earthquake impact mapping from drones in Gairagaun, Pubichauki rural municipality
  ward-3, Doti, Nepal (November 2022)
version: null
vulnerability: null
---
