---
attributions:
- entity:
    affiliation: null
    email: null
    name: OpenStreetMap (OSM)
    url: https://data.humdata.org/dataset/japan-road-surface-data
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: HeiGIT deep learning model
    url: https://data.humdata.org/dataset/japan-road-surface-data
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: HeiGIT (Heidelberg Institute for Geoinformation Technology)
  url: https://data.humdata.org/dataset/japan-road-surface-data
creator:
  affiliation: null
  email: null
  name: HeiGIT (Heidelberg Institute for Geoinformation Technology)
  url: https://data.humdata.org/dataset/japan-road-surface-data
dataset_id: rdls_exp-jpn_heigit_roadsurfacedata_20241107
description: 'This dataset provides detailed information on road surfaces from OpenStreetMap
  (OSM) data, distinguishing between **paved** and **unpaved** surfaces across the
  region. This information is based on road surface prediction derived from hybrid
  deep learning approach. For more information on Methods, refer to the [paper](http://arxiv.org/abs/2410.19874)
  Roughly 2.3432 million km of roads are mapped in OSM in this region. Based on AI-mapped
  estimates the share of paved and unpaved roads is approximately 0.4029 and 0.0294
  (in million kms), corressponding to 17.1957% and 1.2527% respectively of the total
  road length in the dataset region. 1.911 million km or 81.5516% of road surface
  information is missing in OSM. In order to fill this gap, Mapillary derived road
  surface dataset provides an additional 0.0405 million km of information (corressponding
  to 2.1189% of total missing information on road surface) It is intended for use
  in transportation planning, infrastructure analysis, climate emissions and geographic
  information system (GIS) applications. This dataset provides comprehensive information
  on road and urban area features, including location, surface quality, and classification
  metadata. This dataset includes attributes from OpenStreetMap (OSM) data, AI predictions
  for road surface, and urban classifications. AI features: pred_class : Model-predicted
  class for the road surface, with values ''paved'' or ''unpaved.'' pred_label : Binary
  label associated with pred_class (0 = paved, 1 = unpaved). osm_surface_class : Classification
  of the surface type from OSM, categorized as ''paved'' or ''unpaved.'' combined_surface_osm_priority
  : Surface classification combining pred_label and surface (OSM) while prioritizing
  the OSM surface tag, classified as ''paved'' or ''unpaved.'' combined_surface_DL_priority
  : Surface classification combining pred_label and surface (OSM) while prioritizing
  DL prediction pred_label , classified as ''paved'' or ''unpaved.'' n_of_predictions_used
  : Number of predictions used for the feature length estimation. predicted_length
  : Predicted length based on the DL model''s estimations, in meters. DL_mean_timestamp
  : Mean timestamp of the predictions used, for comparison. OSM features may have
  these attributes(Learn what tags mean here ): name : Name of the feature, if available
  in OSM. name:en : Name of the feature in English, if available in OSM. name:* (in
  local language) : Name of the feature in the local official language, where available.
  highway : Road classification based on OSM tags (e.g., residential, motorway, footway).
  surface : Description of the surface material of the road (e.g., asphalt, gravel,
  dirt). smoothness : Assessment of surface smoothness (e.g., excellent, good, intermediate,
  bad). width : Width of the road, where available. lanes : Number of lanes on the
  road. oneway : Indicates if the road is one-way (yes or no). bridge : Specifies
  if the feature is a bridge (yes or no). layer : Indicates the layer of the feature
  in cases where multiple features are stacked (e.g., bridges, tunnels). source :
  Source of the data, indicating the origin or authority of specific attributes. Urban
  classification features may have these attributes: continent : The continent where
  the data point is located (e.g., Europe, Asia). country_iso_a2 : The ISO Alpha-2
  code representing the country (e.g., ''US'' for the United States). urban : Binary
  indicator for urban areas based on the GHSU Urban Layer 2019. (0 = rural, 1 = urban)
  urban_area : Name of the urban area or city where the data point is located. osm_id
  : Unique identifier assigned by OpenStreetMap (OSM) to each feature. osm_type :
  Type of OSM element (e.g., node, way, relation). The data originates from OpenStreetMap
  (OSM) and is augmented with model predictions using images downloaded from Mapillary
  in combination with the GHSU Global Human Settlement Urban Layer 2019 and AFRICAPOLIS2020
  urban layer. This dataset is one of many HeiGIT exports on HDX . See the HeiGIT
  website for more information. We are looking forward to hearing about your use-case!
  Feel free to reach out to us and tell us about your research at communications@heigit.org
  - we would be happy to amplify your work.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/japan-road-surface-data]'
details: null
exposure:
- asset_type:
    description: Road network classified by surface type (paved vs unpaved) across
      Japan
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
license: https://opendatacommons.org/licenses/odbl/1-0/
lineage:
  description: Road network geometry and attributes were extracted from OpenStreetMap
    data covering Japan. A hybrid deep learning model was applied to classify road
    surfaces into paved and unpaved categories, generating surface type predictions
    for the entire mapped road network. The resulting dataset provides infrastructure
    exposure data with surface classification suitable for humanitarian access and
    logistics planning.
  sources:
  - id: source_1
    license: null
    name: OpenStreetMap (OSM)
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_2
    license: null
    name: HeiGIT deep learning model
    risk_data_type:
    - exposure
    type: model
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/japan-road-surface-data
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
  description: 'Japan: Road Surface Data (GeoJSON data for Japan.)'
  download_url: https://downloads.ohsome.org/hdx/mapillary_road_surface/heigit_jpn_roadsurface_lines.geojson
  format: null
  id: resource_5f15ae18
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Japan GeoJSON Resource
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Japan: Road Surface Data (Geopackage data for Japan.)'
  download_url: https://downloads.ohsome.org/hdx/mapillary_road_surface/heigit_jpn_roadsurface_lines.gpkg
  format: null
  id: resource_eae8f4e0
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Japan GeoPackage Resource
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-jpn_heigit_roadsurfacedata_20241107
spatial:
  bbox: null
  centroid: null
  countries:
  - JPN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2024-11-07'
temporal_resolution: null
title: 'Japan: Road Surface Data'
version: null
vulnerability: null
---
