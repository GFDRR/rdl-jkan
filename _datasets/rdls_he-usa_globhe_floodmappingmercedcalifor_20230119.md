---
attributions:
- entity:
    affiliation: null
    email: null
    name: GLOBHE
    url: https://data.humdata.org/dataset/flood-mapping-by-drones-in-merced-california-january-2023
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Globhe Drones
  url: https://data.humdata.org/dataset/flood-mapping-by-drones-in-merced-california-january-2023
creator:
  affiliation: null
  email: null
  name: Globhe Drones
  url: https://data.humdata.org/dataset/flood-mapping-by-drones-in-merced-california-january-2023
dataset_id: rdls_he-usa_globhe_floodmappingmercedcalifor_20230119
description: "Several weeks of storms in January 2023 have caused significant damage\
  \ across California, with mudslides and flooding resulting in at least 19 dead and\
  \ widespread damage to infrastructure. Drone experts at GLOBHE have activated drone\
  \ operators in the region, capturing critical data in most affected areas and making\
  \ it accessible to all the authorities, NGOs, and volunteers who now scramble to\
  \ assist. The donated high-quality drone data is available to all entities working\
  \ to support the region, easily accessible here. The datasets includes one high-resolution\
  \ orthomosaic and six 360\xB0 panoramas to show the impact of floodings in the area.\
  \ 'Our thoughts are with everyone affected by the storms and all those who work\
  \ hard to rescue, repair, and rebuild across the affected areas,' says Napoleon\
  \ Bergstr\xF6m, COO at GLOBHE. As a global leader in connecting local drone operators\
  \ with organizations in need of accurate drone data, GLOBHE works together with\
  \ leading organizations to prevent and respond to natural disasters, often in hard-to-access\
  \ areas across the world. 'Access to high-quality imaging can give critical data\
  \ on damage to housing, infrastructure, and nature, and make it easier to make the\
  \ right decisions and help those affected,' says Napoleon Bergstr\xF6m, COO at GLOBHE.\
  \ 'That is why our team will work hard to provide this data.' From January 24, the\
  \ data of affected areas in California is freely available here. About GLOBHE: GLOBHE\
  \ is leading organizations to make better decisions through drone data. Through\
  \ a single platform, the company offers organizations accurate and actionable drone\
  \ data from anywhere in the world. GLOBHE's platform is a leading curated marketplace\
  \ connecting local drone operators with organizations with the need for drone data\
  \ of the highest quality. By creating the sharpest view of reality, Globhe enriches\
  \ our communities and impacts our planet. For more information, please visit https://globhe.com/.\
  \ MORE CROWDDRONING BY GLOBHE Web: https://globhe.com/ Facebook: https://www.facebook.com/Crowddroning\
  \ Twitter: https://twitter.com/globhedrones Instagram: https://www.instagram.com/globhedrones/\
  \ LinkedIn: https://www.linkedin.com/company/globhedrones/. [Source: This metadata\
  \ record was automatically extracted from the Humanitarian Data Exchange (HDX);\
  \ Original dataset: https://data.humdata.org/dataset/flood-mapping-by-drones-in-merced-california-january-2023]"
details: null
exposure:
- asset_type:
    description: Building footprints and structures visible in high-resolution orthomosaic
      imagery
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
      quantity_kind: area
      unit: null
- asset_type:
    description: Infrastructure features (roads, utilities) visible in aerial imagery
    id: infrastructure
    scheme: null
    title: null
    uri: null
  category: infrastructure
  id: exposure_2
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: area
      unit: null
hazard:
  event_sets_by_hazard_type:
    flood:
    - analysis_type: empirical
      calculation_method: observed
      event_count: 0
      events: []
      frequency_distribution: null
      hazards:
      - classification: null
        id: hazard_1
        intensity_measure: wd:m
        process: fluvial_flood
        trigger: null
        type: flood
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: "Drone operators from GLOBHE conducted aerial surveys of flood-affected\
    \ areas in Merced, California in January 2023, capturing high-resolution orthomosaic\
    \ imagery (5cm resolution) and 360\xB0 panoramic photographs. The georeferenced\
    \ imagery documents flood extent, inundated infrastructure, and damaged buildings\
    \ for emergency response and damage assessment purposes."
  sources:
  - id: source_1
    license: null
    name: GLOBHE
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/flood-mapping-by-drones-in-merced-california-january-2023
  rel: source
loss:
  losses: []
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
  description: "High-resolution 360\xB0 panorama showing the impact of floodings in\
    \ the area (Merced, California), captured in January 2023."
  download_url: https://data.humdata.org/dataset/8829829a-85fa-412f-a8ef-03a2a28478dd/resource/bc64f821-505e-48ff-9732-0e4cb957ce43/download/dji_0177.jpg
  format: JPEG
  id: resource_bc64f821
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: California_flood_Merced_panorama1.JPG
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "High-resolution 360\xB0 panorama showing the impact of floodings in\
    \ the area (Merced, California), captured in January 2023."
  download_url: https://data.humdata.org/dataset/8829829a-85fa-412f-a8ef-03a2a28478dd/resource/333ad8fb-e115-40b5-b8cb-2cc20ee4354e/download/dji_0176.jpg
  format: JPEG
  id: resource_333ad8fb
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: California_flood_Merced_panorama2.JPG
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "High-resolution 360\xB0 panorama showing the impact of floodings in\
    \ the area (Merced, California), captured in January 2023."
  download_url: https://data.humdata.org/dataset/8829829a-85fa-412f-a8ef-03a2a28478dd/resource/ee51b63d-7546-416b-9a36-274a7a9941c9/download/dji_0175.jpg
  format: JPEG
  id: resource_ee51b63d
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: California_flood_Merced_panorama3.JPG
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "High-resolution 360\xB0 panorama showing the impact of floodings in\
    \ the area (Merced, California), captured in January 2023."
  download_url: https://data.humdata.org/dataset/8829829a-85fa-412f-a8ef-03a2a28478dd/resource/0d8730c6-48fe-4d3a-8a9b-3c0c538192e0/download/dji_0174.jpg
  format: JPEG
  id: resource_0d8730c6
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: California_flood_Merced_panorama4.JPG
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: High-resolution orthomosaic map showing the impact of floodings in
    the area (Merced, California), captured in January 2023. GSD of 5 cm/px.
  download_url: https://data.humdata.org/dataset/8829829a-85fa-412f-a8ef-03a2a28478dd/resource/c37af110-915b-4ba7-a530-d9655db40fb4/download/california_orthomosaic_5cm.tif
  format: null
  id: resource_c37af110
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: California_Merced_orthomosaic_5cm.tif
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-usa_globhe_floodmappingmercedcalifor_20230119
spatial:
  bbox: null
  centroid: null
  countries:
  - USA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2023-01-19'
temporal_resolution: null
title: United States - Flood mapping by drones in Merced, California (January 2023)
version: null
vulnerability: null
---
