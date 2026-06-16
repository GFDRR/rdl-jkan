---
attributions:
- entity:
    affiliation: null
    email: null
    name: OpenStreetMap (OSM)
    url: https://data.humdata.org/dataset/united-states-of-america-road-surface-data
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Mapillary street-view imagery
    url: https://data.humdata.org/dataset/united-states-of-america-road-surface-data
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: HeiGIT (Heidelberg Institute for Geoinformation Technology)
  url: https://data.humdata.org/dataset/united-states-of-america-road-surface-data
creator:
  affiliation: null
  email: null
  name: HeiGIT (Heidelberg Institute for Geoinformation Technology)
  url: https://data.humdata.org/dataset/united-states-of-america-road-surface-data
dataset_id: rdls_exp-usa_heigit_americaroadsurfacedata_20241107
description: 'This dataset provides detailed information on road surfaces from OpenStreetMap
  (OSM) data, distinguishing between **paved** and **unpaved** surfaces across the
  region. This information is based on road surface prediction derived from hybrid
  deep learning approach. For more information on Methods, refer to the [paper](http://arxiv.org/abs/2410.19874)
  Roughly 111.7039 million km of roads are mapped in OSM in this region. Based on
  AI-mapped estimates the share of paved and unpaved roads is approximately 36.2779
  and 13.31 (in million kms), corressponding to 32.4768% and 11.9154% respectively
  of the total road length in the dataset region. 72.6432 million km or 65.0319% of
  road surface information is missing in OSM. In order to fill this gap, Mapillary
  derived road surface dataset provides an additional 5.0864 million km of information
  (corressponding to 7.0019% of total missing information on road surface) It is intended
  for use in transportation planning, infrastructure analysis, climate emissions and
  geographic information system (GIS) applications. This dataset provides comprehensive
  information on road and urban area features, including location, surface quality,
  and classification metadata. This dataset includes attributes from OpenStreetMap
  (OSM) data, AI predictions for road surface, and urban classifications. AI features:
  pred_class : Model-predicted class for the road surface, with values ''paved'' or
  ''unpaved.'' pred_label : Binary label associated with pred_class (0 = paved, 1
  = unpaved). osm_surface_class : Classification of the surface type from OSM, categorized
  as ''paved'' or ''unpaved.'' combined_surface_osm_priority : Surface classification
  combining pred_label and surface (OSM) while prioritizing the OSM surface tag, classified
  as ''paved'' or ''unpaved.'' combined_surface_DL_priority : Surface classification
  combining pred_label and surface (OSM) while prioritizing DL prediction pred_label
  , classified as ''paved'' or ''unpaved.'' n_of_predictions_used : Number of predictions
  used for the feature length estimation. predicted_length : Predicted length based
  on the DL model''s estimations, in meters. DL_mean_timestamp : Mean timestamp of
  the predictions used, for comparison. OSM features may have these attributes(Learn
  what tags mean here ): name : Name of the feature, if available in OSM. name:en
  : Name of the feature in English, if available in OSM. name:* (in local language)
  : Name of the feature in the local official language, where available. highway :
  Road classification based on OSM tags (e.g., residential, motorway, footway). surface
  : Description of the surface material of the road (e.g., asphalt, gravel, dirt).
  smoothness : Assessment of surface smoothness (e.g., excellent, good, intermediate,
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
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/united-states-of-america-road-surface-data]'
details: null
exposure:
- asset_type:
    description: Road network classified by surface type (paved vs unpaved) across
      the United States
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
    for the United States. A hybrid deep learning model trained on Mapillary street-view
    imagery was applied to classify road surfaces as paved or unpaved, generating
    AI-predicted surface type estimates for the entire road network.
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
    name: Mapillary street-view imagery
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/united-states-of-america-road-surface-data
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
  description: 'United States of America: Road Surface Data (Geopackage file for United
    states of america)'
  download_url: https://warm.storage.heigit.org/heigit-hdx-public/mapillary_road_surface_missing_countries/heigit_usa_roadsurface_lines_36.gpkg
  format: null
  id: resource_80fa23ca
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: United states of america GPKG heigit_usa_roadsurface_lines_36.gpkg
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States of America: Road Surface Data (Geopackage file for United
    states of america)'
  download_url: https://warm.storage.heigit.org/heigit-hdx-public/mapillary_road_surface_missing_countries/heigit_usa_roadsurface_lines_20.gpkg
  format: null
  id: resource_338da1c0
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: United states of america GPKG heigit_usa_roadsurface_lines_20.gpkg
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States of America: Road Surface Data (GeoJSON file for United
    states of america)'
  download_url: https://warm.storage.heigit.org/heigit-hdx-public/mapillary_road_surface_missing_countries/heigit_usa_roadsurface_lines_39.geojson
  format: null
  id: resource_c197d28c
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: United states of america GeoJSON heigit_usa_roadsurface_lines_39.geojson
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States of America: Road Surface Data (Geopackage file for United
    states of america)'
  download_url: https://warm.storage.heigit.org/heigit-hdx-public/mapillary_road_surface_missing_countries/heigit_usa_roadsurface_lines_3.gpkg
  format: null
  id: resource_f78145bb
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: United states of america GPKG heigit_usa_roadsurface_lines_3.gpkg
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States of America: Road Surface Data (GeoJSON file for United
    states of america)'
  download_url: https://warm.storage.heigit.org/heigit-hdx-public/mapillary_road_surface_missing_countries/heigit_usa_roadsurface_lines_27.geojson
  format: null
  id: resource_6e71b9e0
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: United states of america GeoJSON heigit_usa_roadsurface_lines_27.geojson
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States of America: Road Surface Data (Geopackage file for United
    states of america)'
  download_url: https://warm.storage.heigit.org/heigit-hdx-public/mapillary_road_surface_missing_countries/heigit_usa_roadsurface_lines_27.gpkg
  format: null
  id: resource_bdfcf00c
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: United states of america GPKG heigit_usa_roadsurface_lines_27.gpkg
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States of America: Road Surface Data (GeoJSON file for United
    states of america)'
  download_url: https://warm.storage.heigit.org/heigit-hdx-public/mapillary_road_surface_missing_countries/heigit_usa_roadsurface_lines_4.geojson
  format: null
  id: resource_1d4d64c9
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: United states of america GeoJSON heigit_usa_roadsurface_lines_4.geojson
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States of America: Road Surface Data (GeoJSON file for United
    states of america)'
  download_url: https://warm.storage.heigit.org/heigit-hdx-public/mapillary_road_surface_missing_countries/heigit_usa_roadsurface_lines_23.geojson
  format: null
  id: resource_76c57767
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: United states of america GeoJSON heigit_usa_roadsurface_lines_23.geojson
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States of America: Road Surface Data (GeoJSON file for United
    states of america)'
  download_url: https://warm.storage.heigit.org/heigit-hdx-public/mapillary_road_surface_missing_countries/heigit_usa_roadsurface_lines_17.geojson
  format: null
  id: resource_bbd726bf
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: United states of america GeoJSON heigit_usa_roadsurface_lines_17.geojson
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States of America: Road Surface Data (Geopackage file for United
    states of america)'
  download_url: https://warm.storage.heigit.org/heigit-hdx-public/mapillary_road_surface_missing_countries/heigit_usa_roadsurface_lines_26.gpkg
  format: null
  id: resource_b35c0474
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: United states of america GPKG heigit_usa_roadsurface_lines_26.gpkg
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States of America: Road Surface Data (Geopackage file for United
    states of america)'
  download_url: https://warm.storage.heigit.org/heigit-hdx-public/mapillary_road_surface_missing_countries/heigit_usa_roadsurface_lines_25.gpkg
  format: null
  id: resource_b60fe42f
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: United states of america GPKG heigit_usa_roadsurface_lines_25.gpkg
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States of America: Road Surface Data (Geopackage file for United
    states of america)'
  download_url: https://warm.storage.heigit.org/heigit-hdx-public/mapillary_road_surface_missing_countries/heigit_usa_roadsurface_lines_18.gpkg
  format: null
  id: resource_20365e91
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: United states of america GPKG heigit_usa_roadsurface_lines_18.gpkg
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States of America: Road Surface Data (Geopackage file for United
    states of america)'
  download_url: https://warm.storage.heigit.org/heigit-hdx-public/mapillary_road_surface_missing_countries/heigit_usa_roadsurface_lines_22.gpkg
  format: null
  id: resource_3ca2edf8
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: United states of america GPKG heigit_usa_roadsurface_lines_22.gpkg
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States of America: Road Surface Data (Geopackage file for United
    states of america)'
  download_url: https://warm.storage.heigit.org/heigit-hdx-public/mapillary_road_surface_missing_countries/heigit_usa_roadsurface_lines_30.gpkg
  format: null
  id: resource_8d4ce99f
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: United states of america GPKG heigit_usa_roadsurface_lines_30.gpkg
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States of America: Road Surface Data (GeoJSON file for United
    states of america)'
  download_url: https://warm.storage.heigit.org/heigit-hdx-public/mapillary_road_surface_missing_countries/heigit_usa_roadsurface_lines_15.geojson
  format: null
  id: resource_e4102e18
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: United states of america GeoJSON heigit_usa_roadsurface_lines_15.geojson
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States of America: Road Surface Data (Geopackage file for United
    states of america)'
  download_url: https://warm.storage.heigit.org/heigit-hdx-public/mapillary_road_surface_missing_countries/heigit_usa_roadsurface_lines_24.gpkg
  format: null
  id: resource_a6ec5d08
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: United states of america GPKG heigit_usa_roadsurface_lines_24.gpkg
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States of America: Road Surface Data (Geopackage file for United
    states of america)'
  download_url: https://warm.storage.heigit.org/heigit-hdx-public/mapillary_road_surface_missing_countries/heigit_usa_roadsurface_lines_14.gpkg
  format: null
  id: resource_e6061944
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: United states of america GPKG heigit_usa_roadsurface_lines_14.gpkg
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States of America: Road Surface Data (Geopackage file for United
    states of america)'
  download_url: https://warm.storage.heigit.org/heigit-hdx-public/mapillary_road_surface_missing_countries/heigit_usa_roadsurface_lines_13.gpkg
  format: null
  id: resource_2719ab87
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: United states of america GPKG heigit_usa_roadsurface_lines_13.gpkg
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States of America: Road Surface Data (Geopackage file for United
    states of america)'
  download_url: https://warm.storage.heigit.org/heigit-hdx-public/mapillary_road_surface_missing_countries/heigit_usa_roadsurface_lines_31.gpkg
  format: null
  id: resource_24ceb8bf
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: United states of america GPKG heigit_usa_roadsurface_lines_31.gpkg
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States of America: Road Surface Data (GeoJSON file for United
    states of america)'
  download_url: https://warm.storage.heigit.org/heigit-hdx-public/mapillary_road_surface_missing_countries/heigit_usa_roadsurface_lines_9.geojson
  format: null
  id: resource_ca71b46f
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: United states of america GeoJSON heigit_usa_roadsurface_lines_9.geojson
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States of America: Road Surface Data (GeoJSON file for United
    states of america)'
  download_url: https://warm.storage.heigit.org/heigit-hdx-public/mapillary_road_surface_missing_countries/heigit_usa_roadsurface_lines_37.geojson
  format: null
  id: resource_e69d6c49
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: United states of america GeoJSON heigit_usa_roadsurface_lines_37.geojson
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States of America: Road Surface Data (GeoJSON file for United
    states of america)'
  download_url: https://warm.storage.heigit.org/heigit-hdx-public/mapillary_road_surface_missing_countries/heigit_usa_roadsurface_lines_38.geojson
  format: null
  id: resource_faec8e00
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: United states of america GeoJSON heigit_usa_roadsurface_lines_38.geojson
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States of America: Road Surface Data (GeoJSON file for United
    states of america)'
  download_url: https://warm.storage.heigit.org/heigit-hdx-public/mapillary_road_surface_missing_countries/heigit_usa_roadsurface_lines_22.geojson
  format: null
  id: resource_5e7bfbdc
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: United states of america GeoJSON heigit_usa_roadsurface_lines_22.geojson
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States of America: Road Surface Data (GeoJSON file for United
    states of america)'
  download_url: https://warm.storage.heigit.org/heigit-hdx-public/mapillary_road_surface_missing_countries/heigit_usa_roadsurface_lines_11.geojson
  format: null
  id: resource_817cff43
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: United states of america GeoJSON heigit_usa_roadsurface_lines_11.geojson
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States of America: Road Surface Data (GeoJSON file for United
    states of america)'
  download_url: https://warm.storage.heigit.org/heigit-hdx-public/mapillary_road_surface_missing_countries/heigit_usa_roadsurface_lines_0.geojson
  format: null
  id: resource_b4026683
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: United states of america GeoJSON heigit_usa_roadsurface_lines_0.geojson
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States of America: Road Surface Data (GeoJSON file for United
    states of america)'
  download_url: https://warm.storage.heigit.org/heigit-hdx-public/mapillary_road_surface_missing_countries/heigit_usa_roadsurface_lines_12.geojson
  format: null
  id: resource_8ea738ee
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: United states of america GeoJSON heigit_usa_roadsurface_lines_12.geojson
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States of America: Road Surface Data (Geopackage file for United
    states of america)'
  download_url: https://warm.storage.heigit.org/heigit-hdx-public/mapillary_road_surface_missing_countries/heigit_usa_roadsurface_lines_33.gpkg
  format: null
  id: resource_4f43b3d2
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: United states of america GPKG heigit_usa_roadsurface_lines_33.gpkg
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States of America: Road Surface Data (GeoJSON file for United
    states of america)'
  download_url: https://warm.storage.heigit.org/heigit-hdx-public/mapillary_road_surface_missing_countries/heigit_usa_roadsurface_lines_10.geojson
  format: null
  id: resource_3652f8a6
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: United states of america GeoJSON heigit_usa_roadsurface_lines_10.geojson
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States of America: Road Surface Data (Geopackage file for United
    states of america)'
  download_url: https://warm.storage.heigit.org/heigit-hdx-public/mapillary_road_surface_missing_countries/heigit_usa_roadsurface_lines_6.gpkg
  format: null
  id: resource_43572d14
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: United states of america GPKG heigit_usa_roadsurface_lines_6.gpkg
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States of America: Road Surface Data (GeoJSON file for United
    states of america)'
  download_url: https://warm.storage.heigit.org/heigit-hdx-public/mapillary_road_surface_missing_countries/heigit_usa_roadsurface_lines_26.geojson
  format: null
  id: resource_e0ce6929
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: United states of america GeoJSON heigit_usa_roadsurface_lines_26.geojson
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States of America: Road Surface Data (Geopackage file for United
    states of america)'
  download_url: https://warm.storage.heigit.org/heigit-hdx-public/mapillary_road_surface_missing_countries/heigit_usa_roadsurface_lines_37.gpkg
  format: null
  id: resource_c0756bd4
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: United states of america GPKG heigit_usa_roadsurface_lines_37.gpkg
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States of America: Road Surface Data (GeoJSON file for United
    states of america)'
  download_url: https://warm.storage.heigit.org/heigit-hdx-public/mapillary_road_surface_missing_countries/heigit_usa_roadsurface_lines_20.geojson
  format: null
  id: resource_447203cb
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: United states of america GeoJSON heigit_usa_roadsurface_lines_20.geojson
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States of America: Road Surface Data (GeoJSON file for United
    states of america)'
  download_url: https://warm.storage.heigit.org/heigit-hdx-public/mapillary_road_surface_missing_countries/heigit_usa_roadsurface_lines_21.geojson
  format: null
  id: resource_4c627138
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: United states of america GeoJSON heigit_usa_roadsurface_lines_21.geojson
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States of America: Road Surface Data (GeoJSON file for United
    states of america)'
  download_url: https://warm.storage.heigit.org/heigit-hdx-public/mapillary_road_surface_missing_countries/heigit_usa_roadsurface_lines_36.geojson
  format: null
  id: resource_81fd92ca
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: United states of america GeoJSON heigit_usa_roadsurface_lines_36.geojson
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States of America: Road Surface Data (GeoJSON file for United
    states of america)'
  download_url: https://warm.storage.heigit.org/heigit-hdx-public/mapillary_road_surface_missing_countries/heigit_usa_roadsurface_lines_32.geojson
  format: null
  id: resource_7161bfc4
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: United states of america GeoJSON heigit_usa_roadsurface_lines_32.geojson
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States of America: Road Surface Data (GeoJSON file for United
    states of america)'
  download_url: https://warm.storage.heigit.org/heigit-hdx-public/mapillary_road_surface_missing_countries/heigit_usa_roadsurface_lines_7.geojson
  format: null
  id: resource_fd0103e2
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: United states of america GeoJSON heigit_usa_roadsurface_lines_7.geojson
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States of America: Road Surface Data (Geopackage file for United
    states of america)'
  download_url: https://warm.storage.heigit.org/heigit-hdx-public/mapillary_road_surface_missing_countries/heigit_usa_roadsurface_lines_21.gpkg
  format: null
  id: resource_3d53b4b6
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: United states of america GPKG heigit_usa_roadsurface_lines_21.gpkg
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States of America: Road Surface Data (Geopackage file for United
    states of america)'
  download_url: https://warm.storage.heigit.org/heigit-hdx-public/mapillary_road_surface_missing_countries/heigit_usa_roadsurface_lines_9.gpkg
  format: null
  id: resource_26147069
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: United states of america GPKG heigit_usa_roadsurface_lines_9.gpkg
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States of America: Road Surface Data (Geopackage file for United
    states of america)'
  download_url: https://warm.storage.heigit.org/heigit-hdx-public/mapillary_road_surface_missing_countries/heigit_usa_roadsurface_lines_19.gpkg
  format: null
  id: resource_59ae60a0
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: United states of america GPKG heigit_usa_roadsurface_lines_19.gpkg
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States of America: Road Surface Data (Geopackage file for United
    states of america)'
  download_url: https://warm.storage.heigit.org/heigit-hdx-public/mapillary_road_surface_missing_countries/heigit_usa_roadsurface_lines_7.gpkg
  format: null
  id: resource_8e342005
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: United states of america GPKG heigit_usa_roadsurface_lines_7.gpkg
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States of America: Road Surface Data (Geopackage file for United
    states of america)'
  download_url: https://warm.storage.heigit.org/heigit-hdx-public/mapillary_road_surface_missing_countries/heigit_usa_roadsurface_lines_10.gpkg
  format: null
  id: resource_05765651
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: United states of america GPKG heigit_usa_roadsurface_lines_10.gpkg
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States of America: Road Surface Data (GeoJSON file for United
    states of america)'
  download_url: https://warm.storage.heigit.org/heigit-hdx-public/mapillary_road_surface_missing_countries/heigit_usa_roadsurface_lines_31.geojson
  format: null
  id: resource_f960b6a5
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: United states of america GeoJSON heigit_usa_roadsurface_lines_31.geojson
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States of America: Road Surface Data (Geopackage file for United
    states of america)'
  download_url: https://warm.storage.heigit.org/heigit-hdx-public/mapillary_road_surface_missing_countries/heigit_usa_roadsurface_lines_4.gpkg
  format: null
  id: resource_cec5c020
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: United states of america GPKG heigit_usa_roadsurface_lines_4.gpkg
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States of America: Road Surface Data (GeoJSON file for United
    states of america)'
  download_url: https://warm.storage.heigit.org/heigit-hdx-public/mapillary_road_surface_missing_countries/heigit_usa_roadsurface_lines_16.geojson
  format: null
  id: resource_d2c67a7a
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: United states of america GeoJSON heigit_usa_roadsurface_lines_16.geojson
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States of America: Road Surface Data (Geopackage file for United
    states of america)'
  download_url: https://warm.storage.heigit.org/heigit-hdx-public/mapillary_road_surface_missing_countries/heigit_usa_roadsurface_lines_17.gpkg
  format: null
  id: resource_484b6ff2
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: United states of america GPKG heigit_usa_roadsurface_lines_17.gpkg
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States of America: Road Surface Data (GeoJSON file for United
    states of america)'
  download_url: https://warm.storage.heigit.org/heigit-hdx-public/mapillary_road_surface_missing_countries/heigit_usa_roadsurface_lines_24.geojson
  format: null
  id: resource_ae5ca441
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: United states of america GeoJSON heigit_usa_roadsurface_lines_24.geojson
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States of America: Road Surface Data (Geopackage file for United
    states of america)'
  download_url: https://warm.storage.heigit.org/heigit-hdx-public/mapillary_road_surface_missing_countries/heigit_usa_roadsurface_lines_28.gpkg
  format: null
  id: resource_100f50a3
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: United states of america GPKG heigit_usa_roadsurface_lines_28.gpkg
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States of America: Road Surface Data (Geopackage file for United
    states of america)'
  download_url: https://warm.storage.heigit.org/heigit-hdx-public/mapillary_road_surface_missing_countries/heigit_usa_roadsurface_lines_34.gpkg
  format: null
  id: resource_acb13b08
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: United states of america GPKG heigit_usa_roadsurface_lines_34.gpkg
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States of America: Road Surface Data (GeoJSON file for United
    states of america)'
  download_url: https://warm.storage.heigit.org/heigit-hdx-public/mapillary_road_surface_missing_countries/heigit_usa_roadsurface_lines_3.geojson
  format: null
  id: resource_2adde068
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: United states of america GeoJSON heigit_usa_roadsurface_lines_3.geojson
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States of America: Road Surface Data (Geopackage file for United
    states of america)'
  download_url: https://warm.storage.heigit.org/heigit-hdx-public/mapillary_road_surface_missing_countries/heigit_usa_roadsurface_lines_23.gpkg
  format: null
  id: resource_f84a5394
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: United states of america GPKG heigit_usa_roadsurface_lines_23.gpkg
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States of America: Road Surface Data (Geopackage file for United
    states of america)'
  download_url: https://warm.storage.heigit.org/heigit-hdx-public/mapillary_road_surface_missing_countries/heigit_usa_roadsurface_lines_38.gpkg
  format: null
  id: resource_6e061ffb
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: United states of america GPKG heigit_usa_roadsurface_lines_38.gpkg
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States of America: Road Surface Data (Geopackage file for United
    states of america)'
  download_url: https://warm.storage.heigit.org/heigit-hdx-public/mapillary_road_surface_missing_countries/heigit_usa_roadsurface_lines_11.gpkg
  format: null
  id: resource_787eb03e
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: United states of america GPKG heigit_usa_roadsurface_lines_11.gpkg
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States of America: Road Surface Data (Geopackage file for United
    states of america)'
  download_url: https://warm.storage.heigit.org/heigit-hdx-public/mapillary_road_surface_missing_countries/heigit_usa_roadsurface_lines_15.gpkg
  format: null
  id: resource_f0299e84
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: United states of america GPKG heigit_usa_roadsurface_lines_15.gpkg
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States of America: Road Surface Data (GeoJSON file for United
    states of america)'
  download_url: https://warm.storage.heigit.org/heigit-hdx-public/mapillary_road_surface_missing_countries/heigit_usa_roadsurface_lines_34.geojson
  format: null
  id: resource_2238c372
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: United states of america GeoJSON heigit_usa_roadsurface_lines_34.geojson
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States of America: Road Surface Data (Geopackage file for United
    states of america)'
  download_url: https://warm.storage.heigit.org/heigit-hdx-public/mapillary_road_surface_missing_countries/heigit_usa_roadsurface_lines_32.gpkg
  format: null
  id: resource_7f6228a5
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: United states of america GPKG heigit_usa_roadsurface_lines_32.gpkg
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States of America: Road Surface Data (Geopackage file for United
    states of america)'
  download_url: https://warm.storage.heigit.org/heigit-hdx-public/mapillary_road_surface_missing_countries/heigit_usa_roadsurface_lines_39.gpkg
  format: null
  id: resource_c5db52d5
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: United states of america GPKG heigit_usa_roadsurface_lines_39.gpkg
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States of America: Road Surface Data (GeoJSON file for United
    states of america)'
  download_url: https://warm.storage.heigit.org/heigit-hdx-public/mapillary_road_surface_missing_countries/heigit_usa_roadsurface_lines_14.geojson
  format: null
  id: resource_fb251daa
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: United states of america GeoJSON heigit_usa_roadsurface_lines_14.geojson
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States of America: Road Surface Data (GeoJSON file for United
    states of america)'
  download_url: https://warm.storage.heigit.org/heigit-hdx-public/mapillary_road_surface_missing_countries/heigit_usa_roadsurface_lines_19.geojson
  format: null
  id: resource_f22fa23b
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: United states of america GeoJSON heigit_usa_roadsurface_lines_19.geojson
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States of America: Road Surface Data (Geopackage file for United
    states of america)'
  download_url: https://warm.storage.heigit.org/heigit-hdx-public/mapillary_road_surface_missing_countries/heigit_usa_roadsurface_lines_0.gpkg
  format: null
  id: resource_af754d74
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: United states of america GPKG heigit_usa_roadsurface_lines_0.gpkg
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States of America: Road Surface Data (GeoJSON file for United
    states of america)'
  download_url: https://warm.storage.heigit.org/heigit-hdx-public/mapillary_road_surface_missing_countries/heigit_usa_roadsurface_lines_8.geojson
  format: null
  id: resource_b8234b4f
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: United states of america GeoJSON heigit_usa_roadsurface_lines_8.geojson
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States of America: Road Surface Data (GeoJSON file for United
    states of america)'
  download_url: https://warm.storage.heigit.org/heigit-hdx-public/mapillary_road_surface_missing_countries/heigit_usa_roadsurface_lines_1.geojson
  format: null
  id: resource_554ed651
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: United states of america GeoJSON heigit_usa_roadsurface_lines_1.geojson
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States of America: Road Surface Data (GeoJSON file for United
    states of america)'
  download_url: https://warm.storage.heigit.org/heigit-hdx-public/mapillary_road_surface_missing_countries/heigit_usa_roadsurface_lines_13.geojson
  format: null
  id: resource_89783d51
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: United states of america GeoJSON heigit_usa_roadsurface_lines_13.geojson
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States of America: Road Surface Data (Geopackage file for United
    states of america)'
  download_url: https://warm.storage.heigit.org/heigit-hdx-public/mapillary_road_surface_missing_countries/heigit_usa_roadsurface_lines_8.gpkg
  format: null
  id: resource_1146bf29
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: United states of america GPKG heigit_usa_roadsurface_lines_8.gpkg
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States of America: Road Surface Data (GeoJSON file for United
    states of america)'
  download_url: https://warm.storage.heigit.org/heigit-hdx-public/mapillary_road_surface_missing_countries/heigit_usa_roadsurface_lines_33.geojson
  format: null
  id: resource_c0d8e32f
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: United states of america GeoJSON heigit_usa_roadsurface_lines_33.geojson
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States of America: Road Surface Data (GeoJSON file for United
    states of america)'
  download_url: https://warm.storage.heigit.org/heigit-hdx-public/mapillary_road_surface_missing_countries/heigit_usa_roadsurface_lines_35.geojson
  format: null
  id: resource_84c13b3f
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: United states of america GeoJSON heigit_usa_roadsurface_lines_35.geojson
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States of America: Road Surface Data (GeoJSON file for United
    states of america)'
  download_url: https://warm.storage.heigit.org/heigit-hdx-public/mapillary_road_surface_missing_countries/heigit_usa_roadsurface_lines_5.geojson
  format: null
  id: resource_b62ad34c
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: United states of america GeoJSON heigit_usa_roadsurface_lines_5.geojson
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States of America: Road Surface Data (Geopackage file for United
    states of america)'
  download_url: https://warm.storage.heigit.org/heigit-hdx-public/mapillary_road_surface_missing_countries/heigit_usa_roadsurface_lines_12.gpkg
  format: null
  id: resource_2265ad12
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: United states of america GPKG heigit_usa_roadsurface_lines_12.gpkg
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States of America: Road Surface Data (GeoJSON file for United
    states of america)'
  download_url: https://warm.storage.heigit.org/heigit-hdx-public/mapillary_road_surface_missing_countries/heigit_usa_roadsurface_lines_28.geojson
  format: null
  id: resource_9adfec79
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: United states of america GeoJSON heigit_usa_roadsurface_lines_28.geojson
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States of America: Road Surface Data (Geopackage file for United
    states of america)'
  download_url: https://warm.storage.heigit.org/heigit-hdx-public/mapillary_road_surface_missing_countries/heigit_usa_roadsurface_lines_16.gpkg
  format: null
  id: resource_6f805516
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: United states of america GPKG heigit_usa_roadsurface_lines_16.gpkg
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States of America: Road Surface Data (GeoJSON file for United
    states of america)'
  download_url: https://warm.storage.heigit.org/heigit-hdx-public/mapillary_road_surface_missing_countries/heigit_usa_roadsurface_lines_29.geojson
  format: null
  id: resource_2ed26a79
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: United states of america GeoJSON heigit_usa_roadsurface_lines_29.geojson
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States of America: Road Surface Data (Geopackage file for United
    states of america)'
  download_url: https://warm.storage.heigit.org/heigit-hdx-public/mapillary_road_surface_missing_countries/heigit_usa_roadsurface_lines_29.gpkg
  format: null
  id: resource_88c95091
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: United states of america GPKG heigit_usa_roadsurface_lines_29.gpkg
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States of America: Road Surface Data (GeoJSON file for United
    states of america)'
  download_url: https://warm.storage.heigit.org/heigit-hdx-public/mapillary_road_surface_missing_countries/heigit_usa_roadsurface_lines_6.geojson
  format: null
  id: resource_d15f3d53
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: United states of america GeoJSON heigit_usa_roadsurface_lines_6.geojson
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States of America: Road Surface Data (GeoJSON file for United
    states of america)'
  download_url: https://warm.storage.heigit.org/heigit-hdx-public/mapillary_road_surface_missing_countries/heigit_usa_roadsurface_lines_30.geojson
  format: null
  id: resource_4f9bad78
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: United states of america GeoJSON heigit_usa_roadsurface_lines_30.geojson
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States of America: Road Surface Data (GeoJSON file for United
    states of america)'
  download_url: https://warm.storage.heigit.org/heigit-hdx-public/mapillary_road_surface_missing_countries/heigit_usa_roadsurface_lines_18.geojson
  format: null
  id: resource_77b4eed7
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: United states of america GeoJSON heigit_usa_roadsurface_lines_18.geojson
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States of America: Road Surface Data (Geopackage file for United
    states of america)'
  download_url: https://warm.storage.heigit.org/heigit-hdx-public/mapillary_road_surface_missing_countries/heigit_usa_roadsurface_lines_5.gpkg
  format: null
  id: resource_d3ab403e
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: United states of america GPKG heigit_usa_roadsurface_lines_5.gpkg
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States of America: Road Surface Data (Geopackage file for United
    states of america)'
  download_url: https://warm.storage.heigit.org/heigit-hdx-public/mapillary_road_surface_missing_countries/heigit_usa_roadsurface_lines_2.gpkg
  format: null
  id: resource_db6c01e9
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: United states of america GPKG heigit_usa_roadsurface_lines_2.gpkg
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States of America: Road Surface Data (Geopackage file for United
    states of america)'
  download_url: https://warm.storage.heigit.org/heigit-hdx-public/mapillary_road_surface_missing_countries/heigit_usa_roadsurface_lines_1.gpkg
  format: null
  id: resource_063dec21
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: United states of america GPKG heigit_usa_roadsurface_lines_1.gpkg
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States of America: Road Surface Data (Geopackage file for United
    states of america)'
  download_url: https://warm.storage.heigit.org/heigit-hdx-public/mapillary_road_surface_missing_countries/heigit_usa_roadsurface_lines_35.gpkg
  format: null
  id: resource_0f0f93da
  media_type: application/geopackage+sqlite3
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: United states of america GPKG heigit_usa_roadsurface_lines_35.gpkg
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States of America: Road Surface Data (GeoJSON file for United
    states of america)'
  download_url: https://warm.storage.heigit.org/heigit-hdx-public/mapillary_road_surface_missing_countries/heigit_usa_roadsurface_lines_2.geojson
  format: null
  id: resource_da294bed
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: United states of america GeoJSON heigit_usa_roadsurface_lines_2.geojson
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States of America: Road Surface Data (GeoJSON file for United
    states of america)'
  download_url: https://warm.storage.heigit.org/heigit-hdx-public/mapillary_road_surface_missing_countries/heigit_usa_roadsurface_lines_25.geojson
  format: null
  id: resource_edf49340
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: United states of america GeoJSON heigit_usa_roadsurface_lines_25.geojson
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-usa_heigit_americaroadsurfacedata_20241107
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
  start: '2024-11-07'
temporal_resolution: null
title: 'United States of America: Road Surface Data'
version: null
vulnerability: null
---
