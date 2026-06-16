---
attributions:
- entity:
    affiliation: null
    email: null
    name: PlanetScope Imagery
    url: https://data.humdata.org/dataset/saint-lucia-planet-road-surface-data
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: OpenStreetMap (OSM)
    url: https://data.humdata.org/dataset/saint-lucia-planet-road-surface-data
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: HeiGIT (Heidelberg Institute for Geoinformation Technology)
  url: https://data.humdata.org/dataset/saint-lucia-planet-road-surface-data
creator:
  affiliation: null
  email: null
  name: HeiGIT (Heidelberg Institute for Geoinformation Technology)
  url: https://data.humdata.org/dataset/saint-lucia-planet-road-surface-data
dataset_id: rdls_exp-lca_heigit_saintluciaplanetroadsurfa_2020
description: "This dataset provides AI-derived road surface type, road width, road\
  \ surface change (unpaved -> paved), and a Humanitarian Passability Index (HPI)\
  \ using PlanetScope satellite imagery (2020 & 2024). The analysis focuses on the\
  \ global arterial road network, defined as OSM highways classified as motorway,\
  \ trunk, primary, and secondary, including their associated _link classes. These\
  \ road types form the backbone of long-distance, high-capacity transportation and\
  \ national connectivity. This dataset supports humanitarian logistics, climate resilience,\
  \ transportation planning, SDG monitoring, infrastructure investment, and large-scale\
  \ accessibility assessments. For more details on methods, refer to the following\
  \ paper: TBA Relationship to the Previous Mapillary-Based Dataset HeiGIT previously\
  \ released a global dataset providing AI-derived surface attributes from Mapillary\
  \ street-level imagery. - The Mapillary dataset provides detailed, ground-level\
  \ information but is limited by uneven imagery availability and regional coverage\
  \ gaps. - The new PlanetScope-based dataset provides near-complete and globally\
  \ consistent coverage along arterial roads, enabling continental and national-scale\
  \ planning. Accuracy & Data Quality The PlanetScope surface model achieved 89.2%\
  \ accuracy, significantly outperforming OSM surface tags (64.7%). This improvement\
  \ reflects rapid infrastructure development and inconsistencies in OSM mapping of\
  \ surface conditions in many regions. Summary of Road Statistics Approximately 0.0002\
  \ million km of arterial roads are mapped in OSM in this region. - Paved roads:\
  \ 0.0002 million km (95.718%) - Unpaved roads: 0.0 million km (0.0%) - Missing OSM\
  \ surface tags: 0.0 million km (0.7347%) - PlanetScope predictions cover: 0.0002\
  \ million km (13028.2428%) of missing data AI-Derived Attributes Included DL Surface\
  \ Prediction 2020 - Paved / Unpaved / Unknown (PlanetScope model) DL Surface Prediction\
  \ 2024 - Paved / Unpaved / Unknown Road Surface Change (2020-2024) - transitions\
  \ from unpaved -> paved Road Width Class - Categorized into 3 classes Humanitarian\
  \ Passability Index (HPI) - Combines surface type and road width Road Width Class\
  \ Summary Class 1 (<3.5 m) - Light vehicles only; high blockage risk Class 2 (3.5-5.5\
  \ m) - Single-lane heavy truck; alternating flow Class 3 (>5.5 m) - Two-lane heavy\
  \ truck; unimpeded flow Humanitarian Passability Index (HPI) HPI Alphanumeric code\
  \ (e.g., P3, U1) HPI Subtype (e.g., PAV_DUAL, UNP_LIGHT) HPI Score 1-6 (1 = highest\
  \ passability, 6 = lowest) HPI Class Summary Paved, Two-Lane (> 5.5 m) - Primary\
  \ Corridor: All-weather, high-capacity supply route. Codes: P3 / PAV_DUAL / Score:\
  \ 1 Paved, Single-Lane (3.5-5.5 m) - Reliable Chokepoint: Slow, but passable in\
  \ most weather conditions. Codes: P2 / PAV_SINGLE / Score: 2 Paved, Light Vehicle\
  \ (< 3.5 m) - Limited Access Route: Usable by small vehicles; impassable for heavy\
  \ trucks. Codes: P1 / PAV_LIGHT / Score: 4 Unpaved, Two-Lane (> 5.5 m) - Vulnerable\
  \ Corridor: High capacity but at risk of rapid degradation in adverse weather. Codes:\
  \ U3 / UNP_DUAL / Score: 3 Unpaved, Single-Lane (3.5-5.5 m) - High-Risk Chokepoint:\
  \ Dry season only; highly vulnerable to weather. Codes: U2 / UNP_SINGLE / Score:\
  \ 5 Unpaved, Light Vehicle (< 3.5 m) - High-Risk Track: Dry season only, 4\xC3\u2014\
  4 required. High risk of impassability. Codes: U1 / UNP_LIGHT / Score: 6 Included\
  \ OSM Attributes Road Segment ID highway classification surface tag OSM road length\
  \ (meters) Geographic Attributes country_iso_a2 continent This dataset integrates\
  \ OSM attributes with deep-learning predictions generated from PlanetScope imagery\
  \ (2020 and 2024) using HeiGIT's large-scale geospatial AI pipelines. Explore more\
  \ HeiGIT datasets on HDX: https://data.humdata.org/organization/heidelberg-institute-for-geoinformation-technology\
  \ More information: https://heigit.org/ We welcome feedback and use-cases. Contact\
  \ us at: communications@heigit.org. [Source: This metadata record was automatically\
  \ extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/saint-lucia-planet-road-surface-data]"
details: null
exposure:
- asset_type:
    description: Road network classified by surface type, width, and humanitarian
      passability derived from satellite imagery
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
hazard: null
license: CC-BY-4.0
lineage:
  description: Road network data from OpenStreetMap was extracted for arterial highways
    in Saint Lucia. Deep learning models were applied to PlanetScope satellite imagery
    from 2020 and 2024 to classify road surface type (paved/unpaved), measure road
    width, detect surface changes, and derive a Humanitarian Passability Index (HPI)
    with risk scoring. The resulting dataset supports humanitarian logistics planning
    and infrastructure resilience assessment.
  sources:
  - id: source_1
    license: null
    name: PlanetScope Imagery
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_2
    license: null
    name: OpenStreetMap (OSM)
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/saint-lucia-planet-road-surface-data
  rel: source
loss: null
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
  description: 'Saint Lucia: Planet Road Surface, Width, and Passability Data (GeoJSON
    file for Saint lucia)'
  download_url: https://warm.storage.heigit.org/heigit-hdx-public/planet_road_data/heigit_LC_planet_roadsurface_lines.geojson
  format: null
  id: resource_922214b3
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Saint lucia GeoJSON heigit_LC_planet_roadsurface_lines.geojson
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Saint Lucia: Planet Road Surface, Width, and Passability Data (Geopackage
    file for Saint lucia)'
  download_url: https://warm.storage.heigit.org/heigit-hdx-public/planet_road_data/heigit_LC_planet_roadsurface_lines.gpkg
  format: null
  id: resource_c329b1a2
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Saint lucia GPKG heigit_LC_planet_roadsurface_lines.gpkg
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-lca_heigit_saintluciaplanetroadsurfa_2020
spatial:
  bbox: null
  centroid: null
  countries:
  - LCA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2024-12-31'
  start: '2020-06-01'
temporal_resolution: null
title: 'Saint Lucia: Planet Road Surface, Width, and Passability Data'
version: null
vulnerability: null
---
