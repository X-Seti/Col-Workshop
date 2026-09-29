#!/usr/bin/env python3
#this belongs in apps/components/Col_Editor/col_workshop.py - Version: 116
# X-Seti - August10 2025 - Converted col editor using gui base template.

"""
components/Col_Editor/col_workshop.py
COL Editor - Main collision editor interface
"""

import os
# Force X11/GLX backend for NVIDIA on Wayland
os.environ['QT_QPA_PLATFORM'] = 'xcb'
os.environ['QSG_RHI_BACKEND'] = 'opengl'
os.environ['LIBGL_ALWAYS_SOFTWARE'] = '0'  # Use hardware acceleration

import sys


# Add project root to path for standalone mode
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(os.path.dirname(current_dir)))
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

# Import PyQt6
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QDialog, QLabel, QPushButton, QTextEdit, QMessageBox, QTableWidgetItem)
from PyQt6.QtCore import Qt, pyqtSignal, QSize, QPoint
from PyQt6.QtGui import QFont, QColor
# QAction location varies by PyQt6 version — try bothQStyledItemDelegate

# Import project modules AFTER path setup
from apps.methods.imgfactory_svg_icons import SVGIconFactory

from apps.gui.tool_menu_mixin import ToolMenuMixin
from apps.methods.gl_viewport_mixin import GLViewportMixin
# COL Workshop parser system

from apps.components.Col_Editor.depends.col_win_func import COLWindowMixin
from apps.components.Col_Editor.depends.col_core_logic_func import COLCoreLogicMixin
from apps.components.Col_Editor.depends.col_setup_ui_func import COLSetupUIMixin, App_name
from apps.components.Col_Editor.depends.col_viewport import COL3DViewport

VIEWPORT_AVAILABLE = True

DEBUG_STANDALONE = False

##Methods list -
# open_col_workshop
# COLWorkshop.__init__
# COLWorkshop._apply_always_on_top
# COLWorkshop._apply_button_mode_to_button
# COLWorkshop._apply_col_btn_display
# COLWorkshop._apply_fonts_to_widgets
# COLWorkshop._apply_to_selected_faces_paint
# COLWorkshop._apply_window_flags
# COLWorkshop._change_format
# COLWorkshop._close_col_tab
# COLWorkshop._compress_surface
# COLWorkshop._copy_model_info
# COLWorkshop._copy_surface
# COLWorkshop._copy_text_to_clipboard
# COLWorkshop._create_action_section
# COLWorkshop._create_info_section
# COLWorkshop._create_level_card
# COLWorkshop._create_new_model
# COLWorkshop._create_preview_widget
# COLWorkshop._create_stat_box
# COLWorkshop._create_stats_grid
# COLWorkshop._cycle_render_mode
# COLWorkshop._cycle_view_render_style
# COLWorkshop._delete_surface
# COLWorkshop._dock_to_main
# COLWorkshop._draw_col_model
# COLWorkshop._duplicate_surface
# COLWorkshop._edit_main_surface
# COLWorkshop._enable_move_mode
# COLWorkshop._enable_name_edit
# COLWorkshop._exit_paint_mode
# COLWorkshop._extract_col_from_img
# COLWorkshop._filter_col_list
# COLWorkshop._find_all_paint_btns
# COLWorkshop._find_col_via_db
# COLWorkshop._focus_search
# COLWorkshop._force_save_col
# COLWorkshop._generate_collision_thumbnail
# COLWorkshop._get_resize_corner
# COLWorkshop._get_resize_direction
# COLWorkshop._get_view_coords
# COLWorkshop._handle_corner_resize
# COLWorkshop._handle_resize
# COLWorkshop._import_selected
# COLWorkshop._import_surface
# COLWorkshop._initialize_features
# COLWorkshop._is_on_draggable_area
# COLWorkshop._launch_theme_settings
# COLWorkshop._load_settings
# COLWorkshop._on_col_selected
# COLWorkshop._on_collision_selected
# COLWorkshop._on_compact_col_selected
# COLWorkshop._on_paint_mode_exited
# COLWorkshop._on_painted_face
# COLWorkshop._on_splitter_moved
# COLWorkshop._open_col_file
# COLWorkshop._open_mipmap_manager
# COLWorkshop._open_paint_editor
# COLWorkshop._open_paint_mat_popup
# COLWorkshop._open_render_settings_dialog
# COLWorkshop._open_settings_dialog
# COLWorkshop._open_surface_edit_dialog
# COLWorkshop._open_surface_paint_dialog
# COLWorkshop._open_surface_type_dialog
# COLWorkshop._paint_cycle_mat
# COLWorkshop._paint_model_onto
# COLWorkshop._pan_preview
# COLWorkshop._paste_surface
# COLWorkshop._pick_background_color
# COLWorkshop._populate_collision_list
# COLWorkshop._populate_compact_col_list
# COLWorkshop._project_model_2d
# COLWorkshop._rebuild_toolbars
# COLWorkshop._refresh_main_window
# COLWorkshop._regenerate_all_thumbnails
# COLWorkshop._reload_surface_table
# COLWorkshop._remove_shadow
# COLWorkshop._rename_shadow_shortcut
# COLWorkshop._render_collision_preview
# COLWorkshop._save_as_col_file
# COLWorkshop._save_col_file
# COLWorkshop._save_surface_name
# COLWorkshop._saveall_file
# COLWorkshop._scan_available_locales
# COLWorkshop._select_model_by_row
# COLWorkshop._set_checkerboard_bg
# COLWorkshop._set_col_buttons_enabled
# COLWorkshop._set_icon_display_mode
# COLWorkshop._set_paint_tool
# COLWorkshop._set_status
# COLWorkshop._set_thumbnail_view
# COLWorkshop._setup_settings_button
# COLWorkshop._show_amiga_locale_error
# COLWorkshop._show_col_info
# COLWorkshop._show_col_search
# COLWorkshop._show_detailed_info
# COLWorkshop._show_model_details
# COLWorkshop._show_paint_toolbar
# COLWorkshop._show_settings_dialog
# COLWorkshop._show_settings_hotkeys
# COLWorkshop._show_shaders_dialog
# COLWorkshop._show_shadow_mesh
# COLWorkshop._show_surface_info
# COLWorkshop._show_window_context_menu
# COLWorkshop._show_workshop_settings
# COLWorkshop._start_thumbnail_spin
# COLWorkshop._stop_thumbnail_spin
# COLWorkshop._tick_thumbnail_spin
# COLWorkshop._toggle_boxes
# COLWorkshop._toggle_col_view
# COLWorkshop._toggle_maximize
# COLWorkshop._toggle_mesh
# COLWorkshop._toggle_spheres
# COLWorkshop._toggle_tearoff
# COLWorkshop._toggle_upscale_native
# COLWorkshop._uncompress_surface
# COLWorkshop._undock_from_main
# COLWorkshop._update_all_buttons
# COLWorkshop._update_cursor
# COLWorkshop._update_dock_button_visibility
# COLWorkshop._update_transform_text_panel_visibility
# COLWorkshop.closeEvent
# COLWorkshop.dragEnterEvent
# COLWorkshop.dragMoveEvent
# COLWorkshop.dropEvent
# COLWorkshop.export_all
# COLWorkshop.export_all_surfaces
# COLWorkshop.export_selected
# COLWorkshop.export_selected_surface
# COLWorkshop.mouseDoubleClickEvent
# COLWorkshop.mouseMoveEvent
# COLWorkshop.mousePressEvent
# COLWorkshop.mouseReleaseEvent
# COLWorkshop.paintEvent
# COLWorkshop.refresh
# COLWorkshop.reload_surface_table
# COLWorkshop.resizeEvent
# COLWorkshop.save_col_file
# COLWorkshop.shadow_dialog
# COLWorkshop.showEvent
# COLWorkshop.show_help
# COLWorkshop.show_settings_dialog
# COLWorkshop.switch_surface_view
# COLWorkshop.toggle_dock_mode


#                                                                              
# Surface.dat parser (used by Surface Data tab in COLWorkshop)
#                                                                              


class COLWorkshop(COLWindowMixin, COLSetupUIMixin, COLCoreLogicMixin, GLViewportMixin, ToolMenuMixin, QWidget): #vers 8
    """COL Workshop - Main window"""

    #    ToolMenuMixin implementation                                      


    workshop_closed = pyqtSignal()
    window_closed = pyqtSignal()

    # Bump whenever the set of ribbon toolbars changes (added/removed/
    # renamed) so a saved layout from an older structure is cleanly
    # rejected by _restore_toolbar_state instead of Qt silently failing
    # to restore it. History: 1 = Transform/Navigation/Render ribbons,
    # 2 = added Name/Format/Shadow Mesh ribbons (replacing the old
    # dual text/icon bottom info panel).
    _RIBBON_LAYOUT_VERSION = 2

    def __init__(self, parent=None, main_window=None): #vers 12
        """initialize_features"""
        if DEBUG_STANDALONE and main_window is None:
            print(App_name + " Initializing ...")

        super().__init__(parent)
        self.setWindowTitle(App_name)
        self.setWindowIcon(SVGIconFactory.col_workshop_icon())
        self.icon_factory = SVGIconFactory()

        self.main_window = main_window

        self.undo_stack = []
        self.button_display_mode = 'both'
        self.icon_display_mode = 'icons_and_text'  # 'icons_and_text'|'icons_only'|'text_only'
        self._col_compact_btns = []   # list of (widget, full_label) for adaptive display
        self.last_save_directory = None
        self.current_col_file = None
        # Thumbnail spin animation state
        self._spin_timer  = None
        self._spin_row    = None
        self._spin_model  = None
        self._spin_yaw    = 0.0
        self._spin_pitch  = 0.0
        self._spin_dyaw   = 1.0
        self._spin_dpitch = 0.2
        # Thumbnail view axis (applied to all static thumbnails)
        self._thumb_yaw   = 0.0    # top-down (XY plane) by default
        self._thumb_pitch = 0.0

        # Set default fonts
        from PyQt6.QtGui import QFont
        default_font = QFont("Fira Sans Condensed", 14)
        self.setFont(default_font)
        self.title_font = QFont("Arial", 14)
        self.panel_font = QFont("Arial", 10)
        self.button_font = QFont("Arial", 10)
        self.infobar_font = QFont("Courier New", 9)
        self.standalone_mode = (main_window is None)

        if main_window and hasattr(main_window, 'app_settings'):
            self.app_settings = main_window.app_settings
        else:
            # FIXED: Create AppSettings for standalone mode
            try:
                from apps.utils.app_settings_system import AppSettings
                self.app_settings = AppSettings()
            except Exception as e:
                print(f"Could not initialize AppSettings: {e}")
                self.app_settings = None
        if hasattr(self.app_settings, 'theme_changed'):
            self.app_settings.theme_changed.connect(self._refresh_icons)
            self.app_settings.theme_changed.connect(self._on_theme_changed)

        self._show_boxes = True
        self._show_mesh = True

        self._checkerboard_size = 16
        self._overlay_opacity = 50
        self.zoom_level = 1.0
        self.pan_offset = QPoint(0, 0)

        self.background_color = self._get_ui_color('viewport_bg')

        self.background_mode = 'solid'
        self.placeholder_text = "No Surface"
        self.setMinimumSize(200, 200)
        preview_widget = False

        # Docking state
        self.is_docked = (main_window is not None)
        self.dock_widget = None
        self.is_overlay = False
        self.overlay_table = None
        self.overlay_tab_index = -1


        self.setWindowTitle(App_name + ": No File")
        self.resize(1400, 800)
        self.use_system_titlebar = False
        self.window_always_on_top = False

        # Window flags
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)

        self._initialize_features()

        # Corner resize variables
        self.dragging = False
        self.drag_position = None
        self.resizing = False
        self.resize_corner = None
        self.corner_size = 20
        self.hover_corner = None

        if parent:
            parent_pos = parent.pos()
            self.move(parent_pos.x() + 50, parent_pos.y() + 80)

        # Paint toolbar attrs — set by _create_paint_bar() called from _create_right_panel
        self.paint_toolbar   = None
        self.paint_mat_combo = None
        self.paint_swatch    = None
        self.paint_undo_btn  = None
        self.paint_exit_btn  = None
        self.tool_paint_btn  = None
        self.tool_dropper_btn = None
        self.tool_fill_btn   = None

        # Setup UI FIRST
        self.setup_ui()
        # Setup hotkeys
        self._setup_hotkeys()

        # Apply theme ONCE at the end
        self._apply_theme()
        self.setAcceptDrops(True)       # .col / .img dropped here open in this workshop


    #    Stub implementations (log until fully implemented)                   


    def _open_surface_type_dialog(self): #vers 1
        """Show surface material type picker for selected model."""
        rows = self.collision_list.selectionModel().selectedRows()
        if not rows or not self.current_col_file: return
        row = rows[0].row()
        item = self.collision_list.item(row, 1)
        if not item: return
        idx = item.data(Qt.ItemDataRole.UserRole)
        if idx is None: return
        model = self.current_col_file.models[idx]
        types = {0:"Default",1:"Tarmac",2:"Gravel",3:"Grass",4:"Sand",5:"Water",
                 6:"Metal",7:"Wood",8:"Concrete",63:"Obstacle"}
        from PyQt6.QtWidgets import QDialog, QVBoxLayout, QListWidget, QDialogButtonBox
        dlg = QDialog(self); dlg.setWindowTitle(f"Surface Type — {model.name}")
        lay = QVBoxLayout(dlg)
        lst = QListWidget()
        for k,v in types.items(): lst.addItem(f"{k:3d}  {v}")
        lay.addWidget(lst)
        btns = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        btns.accepted.connect(dlg.accept); btns.rejected.connect(dlg.reject)
        lay.addWidget(btns)
        dlg.exec()


    def _open_paint_editor(self): #vers 4
        """Enter paint mode immediately — no dialog.
        All material selection happens in the viewport overlay."""
        if not self.current_col_file:
            from PyQt6.QtWidgets import QMessageBox
            QMessageBox.warning(self, "No File", "Load a COL file first.")
            return
        model = self._get_selected_model()
        if model is None:
            from PyQt6.QtWidgets import QMessageBox
            QMessageBox.warning(self, "No Model Selected",
                "Select a model in the list first.")
            return
        if not getattr(model, 'faces', []):
            from PyQt6.QtWidgets import QMessageBox
            QMessageBox.information(self, "No Mesh Faces",
                f"'{model.name}' has no mesh faces to paint.")
            return

        vp = getattr(self, 'preview_widget', None)
        if not vp:
            return

        models  = getattr(self.current_col_file, 'models', [])
        model_idx = models.index(model) if model in models else -1

        # Use last active mat or default 0
        mat_id  = getattr(self, '_paint_active_mat', 0)

        # Push one undo snapshot on entry
        if model_idx >= 0:
            self._push_undo(model_idx, f"Enter paint mode")

        # Cache the full material list for this model's version
        try:
            from apps.methods.col_materials import get_materials_for_version, COLGame
            ver     = getattr(getattr(model,'version',None),'value',3) if model else 3
            game    = COLGame.VC if ver == 1 else COLGame.SA
            self._paint_mat_list = get_materials_for_version(game, include_procedural=True)
        except Exception:
            self._paint_mat_list = [(i, f"Material {i}", "808080") for i in range(64)]

        # Set current index into the list
        mat_ids = [m[0] for m in self._paint_mat_list]
        self._paint_mat_idx = mat_ids.index(mat_id) if mat_id in mat_ids else 0
        mat_id = self._paint_mat_list[self._paint_mat_idx][0]
        self._paint_active_mat = mat_id

        # Enter viewport paint mode
        vp.set_paint_mode(True, mat_id)
        vp.on_face_selected = self._on_painted_face
        vp._paint_material  = mat_id
        vp.update()  # draw overlay immediately

        # Update paint button to show exit state
        for btn in self._find_all_paint_btns():
            if hasattr(btn, 'clicked'):
                try: btn.clicked.disconnect()
                except: pass
                btn.clicked.connect(self._exit_paint_mode)
                btn.setStyleSheet("color:palette(link); font-weight:bold;")
            else:
                try: btn.triggered.disconnect()
                except: pass
                btn.triggered.connect(self._exit_paint_mode)
            btn.setText("[ ] Exit Paint")

        self._set_status(
            "Paint mode — click faces to paint | change material  "
            "|  Shift+drag to select  |  Esc to exit")


    def _open_paint_mat_popup(self): #vers 2
        """Searchable material popup anchored below the mat chip.
        Closes on item click, X button, or focus loss."""
        from PyQt6.QtWidgets import (QListWidget, QListWidgetItem, QFrame,
                                     QVBoxLayout, QHBoxLayout, QLineEdit,
                                     QPushButton, QLabel)
        from PyQt6.QtCore import Qt
        from PyQt6.QtGui import QColor

        lst = getattr(self, '_paint_mat_list', [])
        if not lst: return

        vp = getattr(self, 'preview_widget', None)
        if not vp: return

        # Close any existing popup
        old = getattr(self, '_mat_popup', None)
        if old:
            try: old.hide(); old.deleteLater()
            except: pass
            self._mat_popup = None

        popup = QFrame(vp)
        popup.setFrameStyle(QFrame.Shape.StyledPanel)
        popup.setStyleSheet(
            "QFrame { background:palette(base); border:1px solid palette(highlight); border-radius:4px; }"
            "QListWidget { background:palette(base); color:palette(windowText); border:none; }"
            "QListWidget::item { padding:2px 4px; }"
            "QListWidget::item:hover { background:palette(alternateBase); }"
            "QListWidget::item:selected { background:palette(highlight); color:palette(highlightedText); }"
            "QLineEdit { background:palette(base); color:palette(windowText); border:1px solid palette(mid); "
            "            border-radius:3px; padding:2px 4px; }"
            "QPushButton { background:transparent; color:palette(link); border:none; "
            "              font-weight:bold; font-size:14px; }"
            "QPushButton:hover { color:palette(highlight); }"
        )

        lay = QVBoxLayout(popup)
        lay.setContentsMargins(6, 4, 6, 6)
        lay.setSpacing(4)

        # Header: search + X
        hdr = QHBoxLayout()
        search = QLineEdit()
        search.setPlaceholderText("Filter materials…")
        search.setFixedHeight(26)
        hdr.addWidget(search)
        close_btn = QPushButton("✕")
        close_btn.setFixedSize(22, 22)
        close_btn.setToolTip("Close")
        hdr.addWidget(close_btn)
        lay.addLayout(hdr)

        lw = QListWidget()
        lw.setFixedHeight(220)
        lw.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        lay.addWidget(lw)

        ws = self

        def _close():  #vers 1
            popup.hide()
            popup.deleteLater()
            ws._mat_popup = None

        close_btn.clicked.connect(_close)

        def _populate(flt=""):  #vers 1
            lw.clear()
            for mid, name, hex_col in lst:
                if flt and flt.lower() not in name.lower() and flt not in str(mid):
                    continue
                item = QListWidgetItem(f"  {mid:3d}  {name}")
                item.setData(Qt.ItemDataRole.UserRole, mid)
                c = QColor(f"#{hex_col}")
                item.setBackground(
                    QColor(max(0,c.red()//4), max(0,c.green()//4),
                           min(255, c.blue()//4 + 15)))
                item.setForeground(c.lighter(200))
                lw.addItem(item)
            # Scroll to current material
            cur_id = getattr(ws, '_paint_active_mat', 0)
            for i in range(lw.count()):
                if lw.item(i).data(Qt.ItemDataRole.UserRole) == cur_id:
                    lw.setCurrentRow(i)
                    lw.scrollToItem(lw.item(i))
                    break

        _populate()
        search.textChanged.connect(_populate)

        def _pick(item):  #vers 1
            mid = item.data(Qt.ItemDataRole.UserRole)
            if mid is None: return
            mat_ids = [m[0] for m in lst]
            ws._paint_mat_idx    = mat_ids.index(mid) if mid in mat_ids else 0
            ws._paint_active_mat = mid
            vp._paint_material   = mid
            vp.update()
            _close()

        lw.itemClicked.connect(_pick)
        lw.itemDoubleClicked.connect(_pick)

        # Position: anchored below the mat chip, aligned to right edge
        W = vp.width()
        _MARGIN = 8; _MAT_W = 200; _ROW1_Y = 4; _CHIP_H = 26; _ARW = 22
        pw = 200   # popup width
        px = W - _MAT_W - _MARGIN + _ARW     # left-align with mat name chip
        py = _ROW1_Y + _CHIP_H + 4           # just below mat row
        # Keep inside viewport
        px = max(4, min(px, W - pw - 4))
        popup.move(px, py)
        popup.resize(pw, 264)
        popup.show()
        popup.raise_()
        self._mat_popup = popup
        search.setFocus()


    def _apply_to_selected_faces_paint(self): #vers 1
        """Apply current paint material to all selected faces (F key in paint mode)."""
        vp = getattr(self, 'preview_widget', None)
        if not vp: return
        sel = sorted(getattr(vp, '_selected_faces', set()))
        if not sel:
            self._set_status("No faces selected — click or drag to select faces first")
            return
        model = self._get_selected_model()
        if not model: return
        models = getattr(self.current_col_file, 'models', [])
        mi = models.index(model) if model in models else -1
        mat_id = getattr(self, '_paint_active_mat', 0)
        if mi >= 0:
            self._push_undo(mi, f"Paint {mat_id} → {len(sel)} selected faces")
        for fi in sel:
            if fi < len(model.faces):
                f = model.faces[fi]
                if hasattr(f.material, 'material_id'):
                    f.material.material_id = mat_id
                else:
                    f.material = mat_id
        vp.update()
        self._set_status(f"Applied material {mat_id} to {len(sel)} selected face(s)")


    def _paint_cycle_mat(self, delta: int): #vers 1
        """Cycle active paint material by delta steps (+1 next / -1 prev)."""
        lst = getattr(self, '_paint_mat_list', [])
        if not lst: return
        idx = getattr(self, '_paint_mat_idx', 0)
        idx = (idx + delta) % len(lst)
        self._paint_mat_idx   = idx
        mat_id, name, hex_col = lst[idx]
        self._paint_active_mat = mat_id
        vp = getattr(self, 'preview_widget', None)
        if vp:
            vp._paint_material = mat_id
            vp.update()
        self._set_status(f"Paint material: {mat_id} — {name}")


    def _on_painted_face(self, face_index, face): #vers 2
        """Called by viewport when a face is painted. Status update only —
        undo state was pushed before entering paint mode."""
        mat_id = self._paint_active_mat if hasattr(self, '_paint_active_mat') else 0
        self._set_status(f"Painted face {face_index} → material {mat_id}  [Esc to exit]")


    def _set_paint_tool(self, mode: str): #vers 1
        """Switch active paint tool: 'paint' | 'dropper' | 'fill'."""
        self._current_paint_tool = mode
        vp = getattr(self, 'preview_widget', None)
        if vp:
            vp._tool_mode = mode
            if mode == 'dropper':
                from PyQt6.QtCore import Qt
                vp.setCursor(Qt.CursorShape.PointingHandCursor)
            elif mode == 'fill':
                from PyQt6.QtCore import Qt
                vp.setCursor(Qt.CursorShape.CrossCursor)
            else:
                from PyQt6.QtCore import Qt
                vp.setCursor(Qt.CursorShape.CrossCursor)
        # Update button check states
        for btn, name in [
            (getattr(self, 'tool_paint_btn', None), 'paint'),
            (getattr(self, 'tool_dropper_btn', None), 'dropper'),
            (getattr(self, 'tool_fill_btn', None), 'fill'),
        ]:
            if btn:
                btn.setChecked(name == mode)
        tool_names = {'paint': 'Paint', 'dropper': 'Dropper (pick material)', 'fill': 'Fill (same material)'}
        self._set_status(f"Tool: {tool_names.get(mode, mode)}")


    def _exit_paint_mode(self): #vers 2
        """Exit paint mode — hide toolbar, restore paint button."""
        # Close material popup if open
        old_popup = getattr(self, '_mat_popup', None)
        if old_popup:
            try: old_popup.hide(); old_popup.deleteLater()
            except: pass
            self._mat_popup = None

        vp = getattr(self, 'preview_widget', None)
        if vp:
            vp.set_paint_mode(False)
            vp.on_face_selected = None

        # Hide QWidget paint bar if it was created, refresh viewport
        tb = getattr(self, 'paint_toolbar', None)
        if tb:
            tb.hide()
        vp = getattr(self, 'preview_widget', None)
        if vp:
            vp.update()

        # Reset paint button in both icon and text panels
        for btn in self._find_all_paint_btns():
            if hasattr(btn, 'clicked'):
                try: btn.clicked.disconnect()
                except: pass
                btn.clicked.connect(self._open_paint_editor)
                btn.setStyleSheet("")
            else:
                try: btn.triggered.disconnect()
                except: pass
                btn.triggered.connect(self._open_paint_editor)
            btn.setText("Paint")
            btn.setChecked(False) if btn.isCheckable() else None

        self._set_status("Paint mode exited.")

    def _on_paint_mode_exited(self): #vers 1
        """Called by viewport Escape key — sync button state."""
        self._exit_paint_mode()


    def _set_status(self, msg: str): #vers 1
        """Write msg to the status label (whichever one exists)."""
        if hasattr(self, 'status_label'):
            self.status_label.setText(msg)
        elif hasattr(self, 'status_bar') and hasattr(self.status_bar, 'showMessage'):
            self.status_bar.showMessage(msg, 3000)
        else:
            print(f"[COL] {msg}")


    def _open_surface_edit_dialog(self): #vers 2
        """Open the COL Mesh Editor for the currently selected model."""
        try:
            from apps.components.Col_Editor.col_mesh_editor import open_col_mesh_editor
            open_col_mesh_editor(self, parent=self)
        except Exception as e:
            import traceback; traceback.print_exc()
            from PyQt6.QtWidgets import QMessageBox
            QMessageBox.warning(self, "Mesh Editor Error", str(e))

    def _cycle_render_mode(self): #vers 2
        """Cycle viewport style wireframe/semi/solid, same as V key."""
        if getattr(self, 'preview_widget', None):
            self.preview_widget._cycle_render_style()


    def _show_shadow_mesh(self): #vers 2
        """Show shadow mesh info for selected model."""
        from PyQt6.QtWidgets import QMessageBox
        model = self._get_selected_model()
        if not model:
            QMessageBox.warning(self, "No Selection", "Select a collision model first.")
            return
        sv = len(getattr(model, 'shadow_verts', []))
        sf = len(getattr(model, 'shadow_faces', []))
        if sv == 0 and sf == 0:
            QMessageBox.information(self, "Shadow Mesh",
                f"'{model.name}' has no shadow mesh data.\n\n"
                "COL3+ models can have a separate low-poly shadow collision mesh.")
        else:
            QMessageBox.information(self, "Shadow Mesh",
                f"Model: {model.name}\n"
                f"Shadow vertices: {sv}\n"
                f"Shadow faces:    {sf}\n\n"
                "Shadow mesh is included in COL3 export.")


    def _open_render_settings_dialog(self): #vers 1
        """Render & background settings dialog."""
        from PyQt6.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout, QLabel,
                                     QComboBox, QSlider, QPushButton, QColorDialog,
                                     QGroupBox, QDialogButtonBox, QCheckBox)
        from PyQt6.QtGui import QColor
        from PyQt6.QtCore import Qt

        pw = getattr(self, 'preview_widget', None)
        if not pw: return

        dlg = QDialog(self)
        dlg.setWindowTitle("Render Settings")
        dlg.setMinimumWidth(360)
        lay = QVBoxLayout(dlg)

        # Object rendering style
        style_grp = QGroupBox("Object Rendering")
        sg = QHBoxLayout(style_grp)
        sg.addWidget(QLabel("Style:"))
        style_combo = QComboBox()
        style_combo.addItems(["Wireframe", "Semi-transparent", "Solid"])
        mapping = {"wireframe":"Wireframe","semi":"Semi-transparent","solid":"Solid"}
        style_combo.setCurrentText(mapping.get(pw._render_style, "Semi-transparent"))
        sg.addWidget(style_combo)
        lay.addWidget(style_grp)

        # Background
        bg_grp = QGroupBox("Background")
        bg = QHBoxLayout(bg_grp)
        r,g,b = pw._bg_color
        bg_preview = QPushButton("  ")
        bg_preview.setFixedSize(60, 28)
        bg_preview.setStyleSheet(f"background-color: rgb({r},{g},{b});")
        def _pick_bg():  #vers 1
            c = QColorDialog.getColor(QColor(r,g,b), dlg, "Background Colour")
            if c.isValid():
                bg_preview.setStyleSheet(f"background-color: {c.name()};")
                bg_preview.setProperty("chosen", (c.red(), c.green(), c.blue()))
        bg_preview.clicked.connect(_pick_bg)
        bg.addWidget(QLabel("Colour:"))
        bg.addWidget(bg_preview)

        scene_cb = QComboBox()
        scene_cb.addItems(["Dark", "Mid", "Light"])
        bg.addWidget(scene_cb)
        lay.addWidget(bg_grp)

        # Buttons
        btns = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok |
                                QDialogButtonBox.StandardButton.Cancel)
        btns.rejected.connect(dlg.reject)
        def _apply():  #vers 1
            s = style_combo.currentText()
            rev = {"Wireframe":"wireframe","Semi-transparent":"semi","Solid":"solid"}
            pw.set_render_style(rev.get(s,"semi"))
            chosen = bg_preview.property("chosen")
            if chosen:
                pw.set_background_color(chosen)
            dlg.accept()
        btns.accepted.connect(_apply)
        lay.addWidget(btns)
        dlg.exec()


    #    Method aliases — drop Qt signal args (*_, **__) before forwarding   
    # These are called from Qt signals that pass e.g. bool(checked) as arg.
    # Target methods take only self, so we must not forward the signal args.
    def _compress_surface(self, *_, **__): return self._compress_col()  #vers 1
    def _copy_surface(self, *_, **__): return self._copy_model_to_clipboard()  #vers 1
    def _delete_surface(self, *_, **__): return self._delete_selected_model()  #vers 1
    def _duplicate_surface(self, *_, **__): return self._duplicate_selected_model()  #vers 1
    def _force_save_col(self, *_, **__): return self._save_file()  #vers 1
    def _import_selected(self, *_, **__): return self._import_col_data()  #vers 1
    def _import_surface(self, *_, **__): return self._import_col_data()  #vers 1
    def _open_col_file(self, *_, **__): return self._open_file()  #vers 1
    def _open_mipmap_manager(self, *_, **__): return self._show_shadow_mesh()  #vers 1
    def _paste_surface(self, *_, **__): return self._paste_model_from_clipboard()  #vers 1
    def _reload_surface_table(self, *_, **__): return self._populate_collision_list()  #vers 1
    def _remove_shadow(self, *_, **__): return self._remove_shadow_mesh()  #vers 1
    def _save_as_col_file(self, *_, **__): return self._save_file()  #vers 1
    def _save_col_file(self, *_, **__): return self._save_file()  #vers 1
    def _saveall_file(self, *_, **__): return self._save_file()  #vers 1
    def _uncompress_surface(self, *_, **__): return self._uncompress_col()  #vers 1
    def export_all(self, *_, **__): return self._export_col_data()  #vers 1
    def export_all_surfaces(self, *_, **__): return self._export_col_data()  #vers 1
    def export_selected(self, *_, **__): return self._export_col_data()  #vers 1
    def export_selected_surface(self, *_, **__): return self._export_col_data()  #vers 1
    def refresh(self, *_, **__): return self._populate_collision_list()  #vers 1
    def reload_surface_table(self, *_, **__): return self._populate_collision_list()  #vers 1
    def save_col_file(self, *a, **kw): return self._save_file(*a, **kw)  #vers 1
    def shadow_dialog(self, *_, **__): return self._create_shadow_mesh()  #vers 2
    def switch_surface_view(self, *_, **__): return self._cycle_render_mode()  #vers 2

    def _change_format(self, *a, **kw): pass  #vers 1
    def _close_col_tab(self, *a, **kw): pass  #vers 1
    def _focus_search(self, *a, **kw): pass  #vers 1
    def _rename_shadow_shortcut(self, *a, **kw): pass  #vers 1
    def _show_detailed_info(self, *a, **kw): pass  #vers 1
    def _show_surface_info(self, *a, **kw): pass  #vers 1
    def show_help(self, *a, **kw): pass  #vers 1
    def show_settings_dialog(self, *a, **kw): pass  #vers 1

    def _set_thumbnail_view(self, yaw, pitch, label="Custom"): #vers 1
        """Change the view angle for all thumbnails and regenerate them."""
        self._thumb_yaw   = float(yaw)
        self._thumb_pitch = float(pitch)
        self._stop_thumbnail_spin()
        self._regenerate_all_thumbnails()
        if hasattr(self, 'main_window') and self.main_window:
            self.main_window.log_message(f"Thumbnail view: {label}")

    def _regenerate_all_thumbnails(self): #vers 1
        """Redraw every thumbnail in both lists at current _thumb_yaw/pitch."""
        if not self.current_col_file:
            return
        models = getattr(self.current_col_file, 'models', [])
        # Compact list
        for row in range(self.col_compact_list.rowCount()):
            item = self.col_compact_list.item(row, 0)
            if item and row < len(models):
                thumb = self._generate_collision_thumbnail(
                    models[row], 64, 64,
                    yaw=self._thumb_yaw, pitch=self._thumb_pitch)
                item.setData(Qt.ItemDataRole.DecorationRole, thumb)
                item.setData(Qt.ItemDataRole.UserRole + 1, True)
        # Detail list
        for row in range(self.collision_list.rowCount()):
            item = self.collision_list.item(row, 0)
            if item and row < len(models):
                thumb = self._generate_collision_thumbnail(
                    models[row], 64, 64,
                    yaw=self._thumb_yaw, pitch=self._thumb_pitch)
                item.setData(Qt.ItemDataRole.DecorationRole, thumb)
                item.setData(Qt.ItemDataRole.UserRole + 1, True)

    def _start_thumbnail_spin(self, row, model): #vers 1
        """Start slowly rotating the thumbnail of the selected row."""
        self._stop_thumbnail_spin()
        self._spin_row   = row
        self._spin_model = model
        self._spin_yaw   = 0.0
        # Random slow axis: yaw + slight pitch drift
        import random
        self._spin_dyaw   = random.uniform(0.8, 1.4)
        self._spin_dpitch = random.uniform(-0.3, 0.3)
        self._spin_pitch  = random.uniform(-20.0, 20.0)
        from PyQt6.QtCore import QTimer
        self._spin_timer = QTimer(self)
        self._spin_timer.setInterval(50)   # 20 fps
        self._spin_timer.timeout.connect(self._tick_thumbnail_spin)
        self._spin_timer.start()

    def _stop_thumbnail_spin(self): #vers 1
        """Stop any running thumbnail rotation."""
        t = getattr(self, '_spin_timer', None)
        if t:
            t.stop()
            t.deleteLater()
            self._spin_timer = None
        self._spin_row   = None
        self._spin_model = None

    def _tick_thumbnail_spin(self): #vers 1
        """Advance the spin angle and update the thumbnail."""
        model = getattr(self, '_spin_model', None)
        row   = getattr(self, '_spin_row',   None)
        if model is None or row is None:
            self._stop_thumbnail_spin()
            return
        # Advance angles
        self._spin_yaw   = (self._spin_yaw + self._spin_dyaw) % 360
        self._spin_pitch = max(-35.0, min(35.0,
            self._spin_pitch + self._spin_dpitch))
        # Flip pitch direction at limits
        if abs(self._spin_pitch) >= 35.0:
            self._spin_dpitch *= -1

        # Only spin if model has geometry
        has_geo = (getattr(model, 'vertices', []) or
                   getattr(model, 'spheres',  []) or
                   getattr(model, 'boxes',    []))
        if not has_geo:
            self._stop_thumbnail_spin()
            return

        # Render thumbnail at current angle
        thumb = self._generate_collision_thumbnail(
            model, 64, 64,
            yaw=self._spin_yaw, pitch=self._spin_pitch)

        # [T] view no longer has thumbnails — spin does nothing visible there
        # The viewport itself rotates via _yaw/_pitch so just stop the timer
        self._stop_thumbnail_spin()

    def _enable_name_edit(self, event, is_alpha): #vers 1
        """Enable name editing on click"""
        self.info_name.setReadOnly(False)
        self.info_name.selectAll()
        self.info_name.setFocus()


# - Panel Creation


    # STUB: dock_btn, tearoff_btn, colour swatch buttons and _svg_to_icon()
    # created icons do not yet update on theme change. Wire to _refresh_icons.

    def _show_workshop_settings(self): #vers 1
        """Show complete workshop settings dialog"""
        from PyQt6.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout, QPushButton,
                                    QTabWidget, QWidget, QGroupBox, QFormLayout,
                                    QSpinBox, QComboBox, QSlider, QLabel, QCheckBox,
                                    QFontComboBox)
        from PyQt6.QtCore import Qt
        from PyQt6.QtGui import QFont

        dialog = QDialog(self)
        dialog.setWindowTitle(App_name + "Settings")
        dialog.setMinimumWidth(650)
        dialog.setMinimumHeight(550)

        layout = QVBoxLayout(dialog)

        # Create tabs
        tabs = QTabWidget()

        # TAB 1: FONTS (FIRST TAB)

        fonts_tab = QWidget()
        fonts_layout = QVBoxLayout(fonts_tab)

        # Default Font
        default_font_group = QGroupBox("Default Font")
        default_font_layout = QHBoxLayout()

        default_font_combo = QFontComboBox()
        default_font_combo.setCurrentFont(self.font())
        default_font_layout.addWidget(default_font_combo)

        default_font_size = QSpinBox()
        default_font_size.setRange(8, 24)
        default_font_size.setValue(self.font().pointSize())
        default_font_size.setSuffix(" pt")
        default_font_size.setFixedWidth(80)
        default_font_layout.addWidget(default_font_size)

        default_font_group.setLayout(default_font_layout)
        fonts_layout.addWidget(default_font_group)

        # Title Font
        title_font_group = QGroupBox("Title Font")
        title_font_layout = QHBoxLayout()

        title_font_combo = QFontComboBox()
        if hasattr(self, 'title_font'):
            title_font_combo.setCurrentFont(self.title_font)
        else:
            title_font_combo.setCurrentFont(QFont("Arial", 14))
        title_font_layout.addWidget(title_font_combo)

        title_font_size = QSpinBox()
        title_font_size.setRange(10, 32)
        title_font_size.setValue(getattr(self, 'title_font', QFont("Arial", 14)).pointSize())
        title_font_size.setSuffix(" pt")
        title_font_size.setFixedWidth(80)
        title_font_layout.addWidget(title_font_size)

        title_font_group.setLayout(title_font_layout)
        fonts_layout.addWidget(title_font_group)

        # Panel Font
        panel_font_group = QGroupBox("Panel Headers Font")
        panel_font_layout = QHBoxLayout()

        panel_font_combo = QFontComboBox()
        if hasattr(self, 'panel_font'):
            panel_font_combo.setCurrentFont(self.panel_font)
        else:
            panel_font_combo.setCurrentFont(QFont("Arial", 10))
        panel_font_layout.addWidget(panel_font_combo)

        panel_font_size = QSpinBox()
        panel_font_size.setRange(8, 18)
        panel_font_size.setValue(getattr(self, 'panel_font', QFont("Arial", 10)).pointSize())
        panel_font_size.setSuffix(" pt")
        panel_font_size.setFixedWidth(80)
        panel_font_layout.addWidget(panel_font_size)

        panel_font_group.setLayout(panel_font_layout)
        fonts_layout.addWidget(panel_font_group)

        # Button Font
        button_font_group = QGroupBox("Button Font")
        button_font_layout = QHBoxLayout()

        button_font_combo = QFontComboBox()
        if hasattr(self, 'button_font'):
            button_font_combo.setCurrentFont(self.button_font)
        else:
            button_font_combo.setCurrentFont(QFont("Arial", 10))
        button_font_layout.addWidget(button_font_combo)

        button_font_size = QSpinBox()
        button_font_size.setRange(8, 16)
        button_font_size.setValue(getattr(self, 'button_font', QFont("Arial", 10)).pointSize())
        button_font_size.setSuffix(" pt")
        button_font_size.setFixedWidth(80)
        button_font_layout.addWidget(button_font_size)

        button_font_group.setLayout(button_font_layout)
        fonts_layout.addWidget(button_font_group)

        # Info Bar Font
        infobar_font_group = QGroupBox("Info Bar Font")
        infobar_font_layout = QHBoxLayout()

        infobar_font_combo = QFontComboBox()
        if hasattr(self, 'infobar_font'):
            infobar_font_combo.setCurrentFont(self.infobar_font)
        else:
            infobar_font_combo.setCurrentFont(QFont("Courier New", 9))
        infobar_font_layout.addWidget(infobar_font_combo)

        infobar_font_size = QSpinBox()
        infobar_font_size.setRange(7, 14)
        infobar_font_size.setValue(getattr(self, 'infobar_font', QFont("Courier New", 9)).pointSize())
        infobar_font_size.setSuffix(" pt")
        infobar_font_size.setFixedWidth(80)
        infobar_font_layout.addWidget(infobar_font_size)

        infobar_font_group.setLayout(infobar_font_layout)
        fonts_layout.addWidget(infobar_font_group)

        fonts_layout.addStretch()
        tabs.addTab(fonts_tab, "Fonts")

        # TAB 2: DISPLAY SETTINGS

        display_tab = QWidget()
        display_layout = QVBoxLayout(display_tab)

        # Button display mode
        button_group = QGroupBox("Button Display Mode")
        button_layout = QVBoxLayout()

        button_mode_combo = QComboBox()
        button_mode_combo.addItems(["Icons + Text", "Icons Only", "Text Only"])
        current_mode = getattr(self, 'button_display_mode', 'both')
        mode_map = {'both': 0, 'icons': 1, 'text': 2}
        button_mode_combo.setCurrentIndex(mode_map.get(current_mode, 0))
        button_layout.addWidget(button_mode_combo)

        button_hint = QLabel("Changes how toolbar buttons are displayed")
        button_hint.setStyleSheet("color: #888; font-style: italic;")
        button_layout.addWidget(button_hint)

        button_group.setLayout(button_layout)
        display_layout.addWidget(button_group)

        # Table display
        table_group = QGroupBox("Surface List Display")
        table_layout = QVBoxLayout()

        show_thumbnails = QCheckBox("Show Surface types")
        show_thumbnails.setChecked(True)
        table_layout.addWidget(show_thumbnails)

        show_warnings = QCheckBox("Show warning icons for suspicious files")
        show_warnings.setChecked(True)
        show_warnings.setToolTip("Shows surface types")
        table_layout.addWidget(show_warnings)

        table_group.setLayout(table_layout)
        display_layout.addWidget(table_group)

        display_layout.addStretch()
        tabs.addTab(display_tab, "Display")


        # TAB 3: placeholder
        # TAB 4: PERFORMANCE

        perf_tab = QWidget()
        perf_layout = QVBoxLayout(perf_tab)

        perf_group = QGroupBox("Performance Settings")
        perf_form = QFormLayout()

        preview_quality = QComboBox()
        preview_quality.addItems(["Low (Fast)", "Medium", "High (Slow)"])
        preview_quality.setCurrentIndex(1)
        perf_form.addRow("Preview Quality:", preview_quality)

        thumb_size = QSpinBox()
        thumb_size.setRange(32, 128)
        thumb_size.setValue(64)
        thumb_size.setSuffix(" px")
        perf_form.addRow("Thumbnail Size:", thumb_size)

        perf_group.setLayout(perf_form)
        perf_layout.addWidget(perf_group)

        # Caching
        cache_group = QGroupBox("Caching")
        cache_layout = QVBoxLayout()

        enable_cache = QCheckBox("Enable surface preview caching")
        enable_cache.setChecked(True)
        cache_layout.addWidget(enable_cache)

        cache_hint = QLabel("Caching improves performance but uses more memory")
        cache_hint.setStyleSheet("color: #888; font-style: italic;")
        cache_layout.addWidget(cache_hint)

        cache_group.setLayout(cache_layout)
        perf_layout.addWidget(cache_group)

        perf_layout.addStretch()
        tabs.addTab(perf_tab, "Performance")

        # TAB 5: PREVIEW SETTINGS (LAST TAB)

        preview_tab = QWidget()
        preview_layout = QVBoxLayout(preview_tab)

        # Zoom Settings
        zoom_group = QGroupBox("Zoom Settings")
        zoom_form = QFormLayout()

        zoom_spin = QSpinBox()
        zoom_spin.setRange(10, 500)
        zoom_spin.setValue(int(getattr(self, 'zoom_level', 1.0) * 100))
        zoom_spin.setSuffix("%")
        zoom_form.addRow("Default Zoom:", zoom_spin)

        zoom_group.setLayout(zoom_form)
        preview_layout.addWidget(zoom_group)

        # Background Settings
        bg_group = QGroupBox("Background Settings")
        bg_layout = QVBoxLayout()

        # Background mode
        bg_mode_layout = QFormLayout()
        bg_mode_combo = QComboBox()
        bg_mode_combo.addItems(["Solid Color", "Checkerboard", "Grid"])
        current_bg_mode = getattr(self, 'background_mode', 'solid')
        mode_idx = {"solid": 0, "checkerboard": 1, "checker": 1, "grid": 2}.get(current_bg_mode, 0)
        bg_mode_combo.setCurrentIndex(mode_idx)
        bg_mode_layout.addRow("Background Mode:", bg_mode_combo)
        bg_layout.addLayout(bg_mode_layout)

        bg_layout.addSpacing(10)

        # Checkerboard size
        cb_label = QLabel("Checkerboard Size:")
        bg_layout.addWidget(cb_label)

        cb_layout = QHBoxLayout()
        cb_slider = QSlider(Qt.Orientation.Horizontal)
        cb_slider.setMinimum(4)
        cb_slider.setMaximum(64)
        cb_slider.setValue(getattr(self, '_checkerboard_size', 16))
        cb_slider.setTickPosition(QSlider.TickPosition.TicksBelow)
        cb_slider.setTickInterval(8)
        cb_layout.addWidget(cb_slider)

        cb_spin = QSpinBox()
        cb_spin.setMinimum(4)
        cb_spin.setMaximum(64)
        cb_spin.setValue(getattr(self, '_checkerboard_size', 16))
        cb_spin.setSuffix(" px")
        cb_spin.setFixedWidth(80)
        cb_layout.addWidget(cb_spin)

        bg_layout.addLayout(cb_layout)

        # Connect checkerboard controls
        #cb_slider.valueChanged.connect(cb_spin.setValue)
        #cb_spin.valueChanged.connect(cb_slider.setValue)

        # Hint
        cb_hint = QLabel("Smaller = tighter pattern, larger = bigger squares")
        cb_hint.setStyleSheet("color: #888; font-style: italic; font-size: 10px;")
        bg_layout.addWidget(cb_hint)

        bg_group.setLayout(bg_layout)
        preview_layout.addWidget(bg_group)

        # Overlay Settings
        overlay_group = QGroupBox("Overlay View Settings")
        overlay_layout = QVBoxLayout()

        overlay_label = QLabel("Overlay Opacity (Wireframe over mesh):")
        overlay_layout.addWidget(overlay_label)

        opacity_layout = QHBoxLayout()
        opacity_slider = QSlider(Qt.Orientation.Horizontal)
        opacity_slider.setMinimum(0)
        opacity_slider.setMaximum(100)
        opacity_slider.setValue(getattr(self, '_overlay_opacity', 50))
        opacity_slider.setTickPosition(QSlider.TickPosition.TicksBelow)
        opacity_slider.setTickInterval(10)
        opacity_layout.addWidget(opacity_slider)

        opacity_spin = QSpinBox()
        opacity_spin.setMinimum(0)
        opacity_spin.setMaximum(100)
        opacity_spin.setValue(getattr(self, '_overlay_opacity', 50))
        opacity_spin.setSuffix(" %")
        opacity_spin.setFixedWidth(80)
        opacity_layout.addWidget(opacity_spin)

        overlay_layout.addLayout(opacity_layout)

        # Connect opacity controls
        #opacity_slider.valueChanged.connect(opacity_spin.setValue)
        #opacity_spin.valueChanged.connect(opacity_slider.setValue)

        # Hint
        opacity_hint = QLabel("0")
        opacity_hint.setStyleSheet("color: #888; font-style: italic; font-size: 10px;")
        overlay_layout.addWidget(opacity_hint)

        overlay_group.setLayout(overlay_layout)
        preview_layout.addWidget(overlay_group)

        preview_layout.addStretch()
        tabs.addTab(preview_tab, "Preview")

        # Add tabs to dialog
        layout.addWidget(tabs)

        # BUTTONS

        btn_layout = QHBoxLayout()
        btn_layout.addStretch()

        # Apply button
        apply_btn = QPushButton("Apply Settings")
        apply_btn.setStyleSheet("""
            QPushButton {
                background: palette(highlight);
                color: white;
                padding: 10px 24px;
                font-weight: bold;
                border-radius: 4px;
                font-size: 13px;
            }
            QPushButton:hover {
                background: palette(highlight);
            }
        """)


        def apply_settings():  #vers 1
            # Adjusted for COL Wireframe, Mesh
            self.setFont(QFont(default_font_combo.currentFont().family(),
                            default_font_size.value()))
            self.title_font = QFont(title_font_combo.currentFont().family(),
                                title_font_size.value())
            self.panel_font = QFont(panel_font_combo.currentFont().family(),
                                panel_font_size.value())
            self.button_font = QFont(button_font_combo.currentFont().family(),
                                    button_font_size.value())
            self.infobar_font = QFont(infobar_font_combo.currentFont().family(),
                                    infobar_font_size.value())

            # Apply fonts to UI
            self._apply_title_font()
            self._apply_panel_font()
            self._apply_button_font()
            self._apply_infobar_font()

            mode_map = {0: 'both', 1: 'icons', 2: 'text'}
            self.button_display_mode = mode_map[button_mode_combo.currentIndex()]

            # EXPORT
            self.default_export_format = self.format_combo.currentText()

            # PREVIEW
            self.zoom_level = zoom_spin.value() / 100.0

            bg_modes = ['solid', 'checkerboard', 'grid']
            self.background_mode = bg_modes[bg_mode_combo.currentIndex()]

            self._checkerboard_size = cb_spin.value()
            self._overlay_opacity = opacity_spin.value()

            # Update preview widget
            if hasattr(self, 'preview_widget'):
                if self.background_mode == 'checkerboard':
                    self.preview_widget.set_checkerboard_background()
                    self.preview_widget._checkerboard_size = self._checkerboard_size
                else:
                    self.preview_widget.set_background_color(self.preview_widget.bg_color)

            # Apply button display mode
            if hasattr(self, '_update_all_buttons'):
                self._update_all_buttons()

            # Refresh display

            if self.main_window and hasattr(self.main_window, 'log_message'):
                self.main_window.log_message("Workshop settings updated successfully")

        apply_btn.clicked.connect(apply_settings)
        btn_layout.addWidget(apply_btn)

        # Close button
        close_btn = QPushButton("Close")
        close_btn.setStyleSheet("padding: 10px 24px; font-size: 13px;")
        close_btn.clicked.connect(dialog.close)
        btn_layout.addWidget(close_btn)

        layout.addLayout(btn_layout)

        # Show dialog
        dialog.exec()


    def _apply_window_flags(self): #vers 1
        """Apply window flags based on settings"""
        # Save current geometry
        current_geometry = self.geometry()
        was_visible = self.isVisible()

        if self.use_system_titlebar:
            # Use system window with title bar
            self.setWindowFlags(
                Qt.WindowType.Window |
                Qt.WindowType.WindowMinimizeButtonHint |
                Qt.WindowType.WindowMaximizeButtonHint |
                Qt.WindowType.WindowCloseButtonHint
            )
        else:
            # Use custom frameless window
            self.setWindowFlags(Qt.WindowType.FramelessWindowHint)

        # Restore geometry and visibility
        self.setGeometry(current_geometry)

        if was_visible:
            self.show()

        if self.main_window and hasattr(self.main_window, 'log_message'):
            mode = "System title bar" if self.use_system_titlebar else "Custom frameless"
            self.main_window.log_message(f"Window mode: {mode}")


    def _show_amiga_locale_error(self): #vers 2
        """Show Amiga Workbench 3.1 style error dialog"""
        from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton, QHBoxLayout
        from PyQt6.QtCore import Qt
        from PyQt6.QtGui import QFont

        dialog = QDialog(self)
        dialog.setWindowTitle("Workbench Request")
        dialog.setFixedSize(450, 150)

        # Amiga Workbench styling
        dialog.setStyleSheet("""
            QDialog {
                background-color: palette(placeholderText);
                border: 2px solid palette(buttonText);
            }
            QLabel {
                color: palette(windowText);
                background-color: palette(placeholderText);
            }
            QPushButton {
                background-color: palette(mid);
                color: palette(windowText);
                border: 2px outset palette(buttonText);
                padding: 5px 15px;
                min-width: 80px;
            }
            QPushButton:pressed {
                border: 2px inset palette(mid);
            }
        """)

        layout = QVBoxLayout(dialog)
        layout.setSpacing(15)
        layout.setContentsMargins(20, 20, 20, 20)

        # Amiga Topaz font style
        amiga_font = QFont("Courier", 10, QFont.Weight.Normal)

        # Error message
        message = QLabel("Workbench 3.1 installer\n\nPlease insert Local disk in any drive")
        message.setFont(amiga_font)
        message.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(message)

        layout.addStretch()

        # Button layout
        button_layout = QHBoxLayout()
        button_layout.addStretch()

        # Retry and Cancel buttons (Amiga style)
        retry_btn = QPushButton("Retry")
        retry_btn.setFont(amiga_font)
        retry_btn.clicked.connect(dialog.accept)
        button_layout.addWidget(retry_btn)

        cancel_btn = QPushButton("Cancel")
        cancel_btn.setFont(amiga_font)
        cancel_btn.clicked.connect(dialog.reject)
        button_layout.addWidget(cancel_btn)

        button_layout.addStretch()
        layout.addLayout(button_layout)

        dialog.exec()


# - Docking functions

    def _update_dock_button_visibility(self): #vers 2
        """Show/hide dock and tearoff buttons based on docked state"""
        if hasattr(self, 'dock_btn'):
            # Hide D button when docked, show when standalone
            self.dock_btn.setVisible(not self.is_docked)

        if hasattr(self, 'tearoff_btn'):
            # T button only visible when docked and not in standalone mode
            self.tearoff_btn.setVisible(self.is_docked and not self.standalone_mode)


    def toggle_dock_mode(self): #vers 2
        """Toggle between docked and standalone mode"""
        if self.is_docked:
            self._undock_from_main()
        else:
            self._dock_to_main()

        self._update_dock_button_visibility()


    def _dock_to_main(self): #vers 9
        """Dock handled by overlay system in imgfactory - IMPROVED"""
        try:
            if hasattr(self, 'is_overlay') and self.is_overlay:
                self.show()
                self.raise_()
                return

            # For proper docking, we need to be called from imgfactory
            # This method should be handled by imgfactory's overlay system
            if self.main_window and hasattr(self.main_window, App_name + '_docked'):
                # If available, use the main window's docking system
                self.main_window.open_col_workshop_docked()
            else:
                # Fallback: just show the window
                self.show()
                self.raise_()

            # Update dock state
            self.is_docked = True
            self._update_dock_button_visibility()
            if hasattr(self, '_middle_btn_row'):
                self._middle_btn_row.setVisible(True)

            if hasattr(self.main_window, 'log_message'):
                self.main_window.log_message(f"{App_name} docked to main window")


        except Exception as e:
            print(f"Error docking: {str(e)}")
            self.show()


    def _undock_from_main(self): #vers 4
        """Undock from overlay mode to standalone window - IMPROVED"""
        try:
            if hasattr(self, 'is_overlay') and self.is_overlay:
                # Switch from overlay to normal window
                self.setWindowFlags(Qt.WindowType.Window)
                self.is_overlay = False
                self.overlay_table = None

            # Set proper window flags for standalone mode
            self.setWindowFlags(Qt.WindowType.Window)
            
            # Ensure proper size when undocking
            if hasattr(self, 'original_size'):
                self.resize(self.original_size)
            else:
                self.resize(1000, 700)  # Reasonable default size
                
            self.is_docked = False
            self._update_dock_button_visibility()
            if hasattr(self, '_middle_btn_row'):
                self._middle_btn_row.setVisible(False)

            self.show()
            self.raise_()

            if hasattr(self.main_window, 'log_message'):
                self.main_window.log_message(f"{App_name} undocked to standalone")
                
        except Exception as e:
            print(f"Error undocking: {str(e)}")
            # Fallback
            self.setWindowFlags(Qt.WindowType.Window)
            self.show()


# - Panel Setup


    #Left side vertical panel


  #  def setup_col_table_structure(workshop): pass
  #  def populate_col_table(workshop, col_file):
  #      for model in col_file.models:
  #          print(f"Model: {model.header.name}")

# - Rest of the logic for the panels


# - Marker 5

    def _toggle_tearoff(self): #vers 2
        """Toggle tear-off state (merge back to IMG Factory) - IMPROVED"""
        try:
            if self.is_docked:
                # Undock from main window
                self._undock_from_main()
                if hasattr(self.main_window, 'log_message'):
                    self.main_window.log_message(f"{App_name} torn off from main window")
            else:
                # Dock back to main window
                self._dock_to_main()
                if hasattr(self.main_window, 'log_message'):
                    self.main_window.log_message(f"{App_name} docked back to main window")
                    
        except Exception as e:
            print(f"Error toggling tear-off: {str(e)}")
            from PyQt6.QtWidgets import QMessageBox
            QMessageBox.warning(self, "Tear-off Error", f"Could not toggle tear-off state:\n{str(e)}")


# - Marker 6


    def _launch_theme_settings(self): #vers 2
        """Launch theme engine from app_settings_system"""
        try:
            from apps.utils.app_settings_system import AppSettings, SettingsDialog

            # Get or create app_settings
            if not hasattr(self, 'app_settings') or self.app_settings is None:
                self.app_settings = AppSettings()
                if not hasattr(self.app_settings, 'current_settings'):
                    print("AppSettings failed to initialize")
                    from PyQt6.QtWidgets import QMessageBox
                    QMessageBox.warning(self, "Error", "Could not initialize theme system")
                    return

            # Launch settings dialog
            dialog = SettingsDialog(self.app_settings, self)

            # Connect theme change signal to apply theme
            dialog.themeChanged.connect(lambda theme: self._apply_theme())

            if dialog.exec():
                # Apply theme after dialog closes
                self._apply_theme()
                print("Theme settings applied")
                if hasattr(self, 'main_window') and self.main_window:
                    if hasattr(self.main_window, 'log_message'):
                        self.main_window.log_message("Theme settings updated")

        except Exception as e:
            print(f"Theme settings error: {e}")
            from PyQt6.QtWidgets import QMessageBox
            QMessageBox.warning(self, "Theme Error", f"Could not load theme system:\n{e}")


    def _show_settings_dialog(self): #vers 6
        """Show comprehensive settings dialog with all tabs including hotkeys"""
        from PyQt6.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout, QTabWidget,
                                    QWidget, QLabel, QPushButton, QGroupBox,
                                    QCheckBox, QSpinBox, QFormLayout, QScrollArea,
                                    QKeySequenceEdit, QComboBox, QMessageBox)
        from PyQt6.QtCore import Qt
        from PyQt6.QtGui import QKeySequence

        dialog = QDialog(self)
        dialog.setWindowTitle(App_name + " Settings")
        dialog.setMinimumWidth(700)
        dialog.setMinimumHeight(600)

        layout = QVBoxLayout(dialog)

        # Create tabs
        tabs = QTabWidget()

        # === DISPLAY TAB ===
        display_tab = QWidget()
        display_layout = QVBoxLayout(display_tab)

        # Thumbnail settings
        thumb_group = QGroupBox("Thumbnail Display")
        thumb_layout = QVBoxLayout()

        thumb_size_layout = QHBoxLayout()
        thumb_size_layout.addWidget(QLabel("Thumbnail size:"))
        thumb_size_spin = QSpinBox()
        thumb_size_spin.setRange(32, 256)
        thumb_size_spin.setValue(self.thumbnail_size if hasattr(self, 'thumbnail_size') else 64)
        thumb_size_spin.setSuffix(" px")
        thumb_size_layout.addWidget(thumb_size_spin)
        thumb_size_layout.addStretch()
        thumb_layout.addLayout(thumb_size_layout)

        thumb_group.setLayout(thumb_layout)
        display_layout.addWidget(thumb_group)

        # Table display settings
        table_group = QGroupBox("Table Display")
        table_layout = QVBoxLayout()

        row_height_layout = QHBoxLayout()
        row_height_layout.addWidget(QLabel("Row height:"))
        row_height_spin = QSpinBox()
        row_height_spin.setRange(50, 200)
        row_height_spin.setValue(getattr(self, 'table_row_height', 100))
        row_height_spin.setSuffix(" px")
        row_height_layout.addWidget(row_height_spin)
        row_height_layout.addStretch()
        table_layout.addLayout(row_height_layout)

        show_grid_check = QCheckBox("Show grid lines")
        show_grid_check.setChecked(getattr(self, 'show_grid_lines', True))
        table_layout.addWidget(show_grid_check)

        table_group.setLayout(table_layout)
        display_layout.addWidget(table_group)

        display_layout.addStretch()
        tabs.addTab(display_tab, "Display")

        # === PREVIEW TAB ===
        preview_tab = QWidget()
        preview_layout = QVBoxLayout(preview_tab)

        # Preview window settings
        preview_window_group = QGroupBox("Preview Window")
        preview_window_layout = QVBoxLayout()

        show_preview_check = QCheckBox("Show preview window by default")
        show_preview_check.setChecked(getattr(self, 'show_preview_default', True))
        show_preview_check.setToolTip("Automatically open preview when selecting surface")
        preview_window_layout.addWidget(show_preview_check)

        auto_refresh_check = QCheckBox("Auto-refresh preview on selection")
        auto_refresh_check.setChecked(getattr(self, 'auto_refresh_preview', True))
        auto_refresh_check.setToolTip("Update preview immediately when clicking surface")
        preview_window_layout.addWidget(auto_refresh_check)

        preview_window_group.setLayout(preview_window_layout)
        preview_layout.addWidget(preview_window_group)

        # Preview size settings
        preview_size_group = QGroupBox("Preview Size")
        preview_size_layout = QVBoxLayout()

        preview_width_layout = QHBoxLayout()
        preview_width_layout.addWidget(QLabel("Default width:"))
        preview_width_spin = QSpinBox()
        preview_width_spin.setRange(200, 1920)
        preview_width_spin.setValue(getattr(self, 'preview_width', 512))
        preview_width_spin.setSuffix(" px")
        preview_width_layout.addWidget(preview_width_spin)
        preview_width_layout.addStretch()
        preview_size_layout.addLayout(preview_width_layout)

        preview_height_layout = QHBoxLayout()
        preview_height_layout.addWidget(QLabel("Default height:"))
        preview_height_spin = QSpinBox()
        preview_height_spin.setRange(200, 1080)
        preview_height_spin.setValue(getattr(self, 'preview_height', 512))
        preview_height_spin.setSuffix(" px")
        preview_height_layout.addWidget(preview_height_spin)
        preview_height_layout.addStretch()
        preview_size_layout.addLayout(preview_height_layout)

        preview_size_group.setLayout(preview_size_layout)
        preview_layout.addWidget(preview_size_group)

        # Preview background
        preview_bg_group = QGroupBox("Preview Background")
        preview_bg_layout = QVBoxLayout()

        bg_combo = QComboBox()
        bg_combo.addItems(["Black", "White", "Gray", "Custom Color"])
        bg_combo.setCurrentText(getattr(self, 'preview_background', 'Checkerboard'))
        preview_bg_layout.addWidget(bg_combo)

        preview_bg_group.setLayout(preview_bg_layout)
        preview_layout.addWidget(preview_bg_group)

        # Preview zoom
        preview_zoom_group = QGroupBox("Preview Zoom")
        preview_zoom_layout = QVBoxLayout()

        fit_to_window_check = QCheckBox("Fit to window by default")
        fit_to_window_check.setChecked(getattr(self, 'preview_fit_to_window', True))
        preview_zoom_layout.addWidget(fit_to_window_check)

        smooth_zoom_check = QCheckBox("Use smooth scaling")
        smooth_zoom_check.setChecked(getattr(self, 'preview_smooth_scaling', True))
        smooth_zoom_check.setToolTip("Better quality but slower for large model mesh")
        preview_zoom_layout.addWidget(smooth_zoom_check)

        preview_zoom_group.setLayout(preview_zoom_layout)
        preview_layout.addWidget(preview_zoom_group)

        preview_layout.addStretch()
        tabs.addTab(preview_tab, "Preview")

        # === EXPORT TAB ===
        export_tab = QWidget()
        export_layout = QVBoxLayout(export_tab)

        # Export format
        format_group = QGroupBox("Default Collision Export Format")
        format_layout = QVBoxLayout()

        format_combo = QComboBox()
        format_combo.addItems(["COL", "COL2", "COL3", "CST", "3DS"])
        format_combo.setCurrentText(getattr(self, 'default_export_format', 'COL'))
        format_layout.addWidget(format_combo)
        format_hint = QLabel("COL recommended for GTAIII/VC, COL2 for SA")
        format_hint.setStyleSheet("color: #888; font-style: italic;")
        format_layout.addWidget(format_hint)

        format_group.setLayout(format_layout)
        export_layout.addWidget(format_group)

        # Export options
        export_options_group = QGroupBox("Export Options")
        export_options_layout = QVBoxLayout()

        preserve_shadow_check = QCheckBox("Preserve Shadow Mesh when exporting")
        preserve_shadow_check.setChecked(getattr(self, 'export_preserve_shadow', True))
        export_options_layout.addWidget(preserve_shadow_check)

        export_shadowm_check = QCheckBox("Export shadow as separate files")
        export_shadowm_check.setChecked(getattr(self, 'export_shadow_separate', False))
        export_shadowm_check.setToolTip("Save each shadow map as _shadow.col, etc.")
        export_options_layout.addWidget(export_shadowm_check)

        create_subfolders_check = QCheckBox("Create subfolders when exporting all")
        create_subfolders_check.setChecked(getattr(self, 'export_create_subfolders', False))
        create_subfolders_check.setToolTip("Organize exports into folders by col type")
        export_options_layout.addWidget(create_subfolders_check)

        export_options_group.setLayout(export_options_layout)
        export_layout.addWidget(export_options_group)

        # Compatibility note
        compat_label = QLabel(
            "Note: Export format support varies by game version. COL1 is compatible with GTA3/VC. COL2/COL3 requires SA or later."
        )
        compat_label.setWordWrap(True)
        compat_label.setStyleSheet("padding: 10px; background-color: palette(base); border-radius: 4px;")
        export_layout.addWidget(compat_label)

        export_layout.addStretch()
        tabs.addTab(export_tab, "Export")

        # === IMPORT TAB ===
        import_tab = QWidget()
        import_layout = QVBoxLayout(import_tab)

        # Import behavior
        import_behavior_group = QGroupBox("Import Behavior")
        import_behavior_layout = QVBoxLayout()

        replace_check = QCheckBox("Replace existing collision with same name")
        replace_check.setChecked(getattr(self, 'import_replace_existing', False))
        import_behavior_layout.addWidget(replace_check)

        auto_format_check = QCheckBox("Automatically select best format")
        auto_format_check.setChecked(getattr(self, 'import_auto_format', True))
        auto_format_check.setToolTip("Choose COL/COL3 based on collision version")
        import_behavior_layout.addWidget(auto_format_check)

        import_behavior_group.setLayout(import_behavior_layout)
        import_layout.addWidget(import_behavior_group)

        # Import format
        import_format_group = QGroupBox("Default Collision Format")
        import_format_layout = QVBoxLayout()

        import_format_combo = QComboBox()
        import_format_combo.addItems(["COL", "COL2", "COL3", "CST", "3DS"])
        import_format_combo.setCurrentText(getattr(self, 'default_import_format', 'COL'))
        import_format_layout.addWidget(import_format_combo)

        format_note = QLabel("COL2/COL3: compression\n, COL type 1 always Uncompressed")
        format_note.setStyleSheet("color: #888; font-style: italic;")
        import_format_layout.addWidget(format_note)

        import_format_group.setLayout(import_format_layout)
        import_layout.addWidget(import_format_group)

        import_layout.addStretch()
        tabs.addTab(import_tab, "Import")

        # === Collision CONSTRAINTS TAB ===
        constraints_tab = QWidget()
        constraints_layout = QVBoxLayout(constraints_tab)

        # Collision naming
        naming_group = QGroupBox("Collision Naming")
        naming_layout = QVBoxLayout()

        name_limit_check = QCheckBox("Enable name length limit")
        name_limit_check.setChecked(getattr(self, 'name_limit_enabled', True))
        name_limit_check.setToolTip("Enforce maximum Collision name length")
        naming_layout.addWidget(name_limit_check)

        char_limit_layout = QHBoxLayout()
        char_limit_layout.addWidget(QLabel("Maximum characters:"))
        char_limit_spin = QSpinBox()
        char_limit_spin.setRange(8, 64)
        char_limit_spin.setValue(getattr(self, 'max_collision_name_length', 32))
        char_limit_spin.setToolTip("RenderWare default is 32 characters")
        char_limit_layout.addWidget(char_limit_spin)
        char_limit_layout.addStretch()
        naming_layout.addLayout(char_limit_layout)

        naming_group.setLayout(naming_layout)
        constraints_layout.addWidget(naming_group)

        # Format support
        format_support_group = QGroupBox("Format Support")
        format_support_layout = QVBoxLayout()

        format_support_group.setLayout(format_support_layout)
        constraints_layout.addWidget(format_support_group)

        constraints_layout.addStretch()
        tabs.addTab(constraints_tab, "Constraints")

        # === KEYBOARD SHORTCUTS TAB ===
        hotkeys_tab = QWidget()
        hotkeys_layout = QVBoxLayout(hotkeys_tab)

        # Add scroll area for hotkeys
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll_widget = QWidget()
        scroll_layout = QVBoxLayout(scroll_widget)

        # File Operations Group
        file_group = QGroupBox("File Operations")
        file_form = QFormLayout()

        hotkey_edit_open = QKeySequenceEdit(self.hotkey_open.key() if hasattr(self, 'hotkey_open') else QKeySequence.StandardKey.Open)
        file_form.addRow("Open col:", hotkey_edit_open)

        hotkey_edit_save = QKeySequenceEdit(self.hotkey_save.key() if hasattr(self, 'hotkey_save') else QKeySequence.StandardKey.Save)
        file_form.addRow("Save col:", hotkey_edit_save)

        hotkey_edit_force_save = QKeySequenceEdit(self.hotkey_force_save.key() if hasattr(self, 'hotkey_force_save') else QKeySequence("Alt+Shift+S"))
        force_save_layout = QHBoxLayout()
        force_save_layout.addWidget(hotkey_edit_force_save)
        force_save_hint = QLabel("(Force save even if unmodified)")
        force_save_hint.setStyleSheet("color: #888; font-style: italic;")
        force_save_layout.addWidget(force_save_hint)
        file_form.addRow("Force Save:", force_save_layout)

        hotkey_edit_save_as = QKeySequenceEdit(self.hotkey_save_as.key() if hasattr(self, 'hotkey_save_as') else QKeySequence.StandardKey.SaveAs)
        file_form.addRow("Save As:", hotkey_edit_save_as)

        hotkey_edit_close = QKeySequenceEdit(self.hotkey_close.key() if hasattr(self, 'hotkey_close') else QKeySequence.StandardKey.Close)
        file_form.addRow("Close:", hotkey_edit_close)

        file_group.setLayout(file_form)
        scroll_layout.addWidget(file_group)

        # Edit Operations Group
        edit_group = QGroupBox("Edit Operations")
        edit_form = QFormLayout()

        hotkey_edit_undo = QKeySequenceEdit(self.hotkey_undo.key() if hasattr(self, 'hotkey_undo') else QKeySequence.StandardKey.Undo)
        edit_form.addRow("Undo:", hotkey_edit_undo)

        hotkey_edit_copy = QKeySequenceEdit(self.hotkey_copy.key() if hasattr(self, 'hotkey_copy') else QKeySequence.StandardKey.Copy)
        edit_form.addRow("Copy Collision:", hotkey_edit_copy)

        hotkey_edit_paste = QKeySequenceEdit(self.hotkey_paste.key() if hasattr(self, 'hotkey_paste') else QKeySequence.StandardKey.Paste)
        edit_form.addRow("Paste Collision:", hotkey_edit_paste)

        hotkey_edit_delete = QKeySequenceEdit(self.hotkey_delete.key() if hasattr(self, 'hotkey_delete') else QKeySequence.StandardKey.Delete)
        edit_form.addRow("Delete:", hotkey_edit_delete)

        hotkey_edit_duplicate = QKeySequenceEdit(self.hotkey_duplicate.key() if hasattr(self, 'hotkey_duplicate') else QKeySequence("Ctrl+D"))
        edit_form.addRow("Duplicate:", hotkey_edit_duplicate)

        hotkey_edit_rename = QKeySequenceEdit(self.hotkey_rename.key() if hasattr(self, 'hotkey_rename') else QKeySequence("F2"))
        edit_form.addRow("Rename:", hotkey_edit_rename)

        edit_group.setLayout(edit_form)
        scroll_layout.addWidget(edit_group)

        # Collision Operations Group
        coll_group = QGroupBox("Collision Operations")
        coll_form = QFormLayout()

        hotkey_edit_import = QKeySequenceEdit(self.hotkey_import.key() if hasattr(self, 'hotkey_import') else QKeySequence("Ctrl+I"))
        coll_form.addRow("Import Collision:", hotkey_edit_import)

        hotkey_edit_export = QKeySequenceEdit(self.hotkey_export.key() if hasattr(self, 'hotkey_export') else QKeySequence("Ctrl+E"))
        coll_form.addRow("Export Collision:", hotkey_edit_export)

        hotkey_edit_export_all = QKeySequenceEdit(self.hotkey_export_all.key() if hasattr(self, 'hotkey_export_all') else QKeySequence("Ctrl+Shift+E"))
        coll_form.addRow("Export All:", hotkey_edit_export_all)

        coll_group.setLayout(coll_form)
        scroll_layout.addWidget(coll_group)

        # View Operations Group
        view_group = QGroupBox("View Operations")
        view_form = QFormLayout()

        hotkey_edit_refresh = QKeySequenceEdit(self.hotkey_refresh.key() if hasattr(self, 'hotkey_refresh') else QKeySequence.StandardKey.Refresh)
        view_form.addRow("Refresh:", hotkey_edit_refresh)

        hotkey_edit_properties = QKeySequenceEdit(self.hotkey_properties.key() if hasattr(self, 'hotkey_properties') else QKeySequence("Alt+Return"))
        view_form.addRow("Properties:", hotkey_edit_properties)

        hotkey_edit_find = QKeySequenceEdit(self.hotkey_find.key() if hasattr(self, 'hotkey_find') else QKeySequence.StandardKey.Find)
        view_form.addRow("Find/Search:", hotkey_edit_find)

        hotkey_edit_help = QKeySequenceEdit(self.hotkey_help.key() if hasattr(self, 'hotkey_help') else QKeySequence.StandardKey.HelpContents)
        view_form.addRow("Help:", hotkey_edit_help)

        view_group.setLayout(view_form)
        scroll_layout.addWidget(view_group)

        scroll_layout.addStretch()

        scroll.setWidget(scroll_widget)
        hotkeys_layout.addWidget(scroll)

        # Reset to defaults button
        reset_layout = QHBoxLayout()
        reset_layout.addStretch()
        reset_hotkeys_btn = QPushButton("Reset to Plasma6 Defaults")

        def reset_hotkeys():  #vers 1
            reply = QMessageBox.question(dialog, "Reset Hotkeys",
                "Reset all keyboard shortcuts to Plasma6 defaults?",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

            if reply == QMessageBox.StandardButton.Yes:
                hotkey_edit_open.setKeySequence(QKeySequence.StandardKey.Open)
                hotkey_edit_save.setKeySequence(QKeySequence.StandardKey.Save)
                hotkey_edit_force_save.setKeySequence(QKeySequence("Alt+Shift+S"))
                hotkey_edit_save_as.setKeySequence(QKeySequence.StandardKey.SaveAs)
                hotkey_edit_close.setKeySequence(QKeySequence.StandardKey.Close)
                hotkey_edit_undo.setKeySequence(QKeySequence.StandardKey.Undo)
                hotkey_edit_copy.setKeySequence(QKeySequence.StandardKey.Copy)
                hotkey_edit_paste.setKeySequence(QKeySequence.StandardKey.Paste)
                hotkey_edit_delete.setKeySequence(QKeySequence.StandardKey.Delete)
                hotkey_edit_duplicate.setKeySequence(QKeySequence("Ctrl+D"))
                hotkey_edit_rename.setKeySequence(QKeySequence("F2"))
                hotkey_edit_import.setKeySequence(QKeySequence("Ctrl+I"))
                hotkey_edit_export.setKeySequence(QKeySequence("Ctrl+E"))
                hotkey_edit_export_all.setKeySequence(QKeySequence("Ctrl+Shift+E"))
                hotkey_edit_refresh.setKeySequence(QKeySequence.StandardKey.Refresh)
                hotkey_edit_properties.setKeySequence(QKeySequence("Alt+Return"))
                hotkey_edit_find.setKeySequence(QKeySequence.StandardKey.Find)
                hotkey_edit_help.setKeySequence(QKeySequence.StandardKey.HelpContents)

        reset_hotkeys_btn.clicked.connect(reset_hotkeys)
        reset_layout.addWidget(reset_hotkeys_btn)
        hotkeys_layout.addLayout(reset_layout)

        tabs.addTab(hotkeys_tab, "Keyboard Shortcuts")

        # Add tabs widget to main layout
        layout.addWidget(tabs)

        # Dialog buttons
        button_layout = QHBoxLayout()
        button_layout.addStretch()

        cancel_btn = QPushButton("Cancel")
        cancel_btn.clicked.connect(dialog.reject)
        button_layout.addWidget(cancel_btn)

        def apply_settings(close_dialog=False):  #vers 1
            """Apply all settings"""
            # Apply display settings
            self.thumbnail_size = thumb_size_spin.value()
            self.table_row_height = row_height_spin.value()
            self.show_grid_lines = show_grid_check.isChecked()

            # Apply preview settings
            self.show_preview_default = show_preview_check.isChecked()
            self.auto_refresh_preview = auto_refresh_check.isChecked()
            self.preview_width = preview_width_spin.value()
            self.preview_height = preview_height_spin.value()
            self.preview_background = bg_combo.currentText()
            self.preview_fit_to_window = fit_to_window_check.isChecked()
            self.preview_smooth_scaling = smooth_zoom_check.isChecked()

            # Apply export settings
            self.default_export_format = format_combo.currentText()
            self.export_preserve_shadow = preserve_shadow_check.isChecked()
            self.export_shadow_separate = export_shadowm_check.isChecked()
            self.export_create_subfolders = create_subfolders_check.isChecked()

            # Apply import settings
            self.import_replace_existing = replace_check.isChecked()
            self.import_auto_format = auto_format_check.isChecked()
            self.default_import_format = import_format_combo.currentText()

            # Apply constraint settings
            self.name_limit_enabled = name_limit_check.isChecked()
            self.max_surface_name_length = char_limit_spin.value()

            # Apply hotkeys
            if hasattr(self, 'hotkey_open'):
                self.hotkey_open.setKey(hotkey_edit_open.keySequence())
            if hasattr(self, 'hotkey_save'):
                self.hotkey_save.setKey(hotkey_edit_save.keySequence())
            if hasattr(self, 'hotkey_force_save'):
                self.hotkey_force_save.setKey(hotkey_edit_force_save.keySequence())
            if hasattr(self, 'hotkey_save_as'):
                self.hotkey_save_as.setKey(hotkey_edit_save_as.keySequence())
            if hasattr(self, 'hotkey_close'):
                self.hotkey_close.setKey(hotkey_edit_close.keySequence())
            if hasattr(self, 'hotkey_undo'):
                self.hotkey_undo.setKey(hotkey_edit_undo.keySequence())
            if hasattr(self, 'hotkey_copy'):
                self.hotkey_copy.setKey(hotkey_edit_copy.keySequence())
            if hasattr(self, 'hotkey_paste'):
                self.hotkey_paste.setKey(hotkey_edit_paste.keySequence())
            if hasattr(self, 'hotkey_delete'):
                self.hotkey_delete.setKey(hotkey_edit_delete.keySequence())
            if hasattr(self, 'hotkey_duplicate'):
                self.hotkey_duplicate.setKey(hotkey_edit_duplicate.keySequence())
            if hasattr(self, 'hotkey_rename'):
                self.hotkey_rename.setKey(hotkey_edit_rename.keySequence())
            if hasattr(self, 'hotkey_import'):
                self.hotkey_import.setKey(hotkey_edit_import.keySequence())
            if hasattr(self, 'hotkey_export'):
                self.hotkey_export.setKey(hotkey_edit_export.keySequence())
            if hasattr(self, 'hotkey_export_all'):
                self.hotkey_export_all.setKey(hotkey_edit_export_all.keySequence())
            if hasattr(self, 'hotkey_refresh'):
                self.hotkey_refresh.setKey(hotkey_edit_refresh.keySequence())
            if hasattr(self, 'hotkey_properties'):
                self.hotkey_properties.setKey(hotkey_edit_properties.keySequence())
            if hasattr(self, 'hotkey_find'):
                self.hotkey_find.setKey(hotkey_edit_find.keySequence())
            if hasattr(self, 'hotkey_help'):
                self.hotkey_help.setKey(hotkey_edit_help.keySequence())

            # Refresh UI with new settings
            if hasattr(self, '_reload_surface_table'):
                self._reload_surface_table()

            if self.main_window and hasattr(self.main_window, 'log_message'):
                self.main_window.log_message("Settings applied")

            if close_dialog:
                dialog.accept()

        apply_btn = QPushButton("Apply")
        apply_btn.clicked.connect(lambda: apply_settings(close_dialog=False))
        button_layout.addWidget(apply_btn)

        ok_btn = QPushButton("OK")
        ok_btn.setDefault(True)
        ok_btn.clicked.connect(lambda: apply_settings(close_dialog=True))
        button_layout.addWidget(ok_btn)

        layout.addLayout(button_layout)

        dialog.exec()


    def _enable_move_mode(self): #vers 2
        """Enable move window mode using system move"""
        handle = self.windowHandle()
        if handle and hasattr(handle, 'startSystemMove'):
            handle.startSystemMove()

    def _toggle_upscale_native(self): #vers 1
        """Toggle upscale native resolution"""
        # Placeholder for upscale native functionality
        print("Upscale Native toggled")

    def _show_shaders_dialog(self): #vers 3
        """Viewport display settings: render style, sphere/box colours and fill alpha."""
        from PyQt6.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout, QLabel,
                                      QRadioButton, QButtonGroup, QPushButton,
                                      QSlider, QGroupBox, QColorDialog, QFrame)
        from PyQt6.QtCore import Qt as _Qt

        pw = getattr(self, 'preview_widget', None)

        dlg = QDialog(self)
        dlg.setWindowTitle("Viewport Display Settings")
        dlg.setFixedSize(320, 380)
        root = QVBoxLayout(dlg)
        root.setSpacing(8)

        # --- Render style ---
        grp_style = QGroupBox("Render Style")
        hlay = QHBoxLayout(grp_style)
        presets = [("Wireframe", "wireframe"), ("Semi", "semi"), ("Solid", "solid")]
        btn_grp = QButtonGroup(dlg)
        vp = pw if pw else self
        cur_style = getattr(vp, '_render_style', 'semi')
        for label, key in presets:
            rb = QRadioButton(label)
            rb.setChecked(key == cur_style)
            def _set_style(checked, k=key, v=vp):  #vers 1
                if checked and hasattr(v, 'set_render_style'):
                    v.set_render_style(k)
            rb.toggled.connect(_set_style)
            btn_grp.addButton(rb)
            hlay.addWidget(rb)
        root.addWidget(grp_style)

        # --- Colour + alpha helper ---
        def _colour_row(parent_layout, label, get_col, set_col, get_alpha, set_alpha):  #vers 1
            row = QHBoxLayout()
            swatch = QFrame()
            swatch.setFixedSize(24, 24)
            r, g, b = get_col()
            swatch.setStyleSheet(f"background: rgb({r},{g},{b}); border: 1px solid #666;")

            lbl = QLabel(label)
            lbl.setFixedWidth(60)

            def _pick():  #vers 1
                r2, g2, b2 = get_col()
                col = QColorDialog.getColor(QColor(r2, g2, b2), dlg, f"Choose {label} colour")
                if col.isValid():
                    set_col((col.red(), col.green(), col.blue()))
                    swatch.setStyleSheet(
                        f"background: rgb({col.red()},{col.green()},{col.blue()}); border: 1px solid #666;")
                    if pw: pw.update()

            pick_btn = QPushButton("Colour")
            pick_btn.setFixedWidth(60)
            pick_btn.clicked.connect(_pick)

            alpha_lbl = QLabel("Fill:")
            slider = QSlider(_Qt.Orientation.Horizontal)
            slider.setRange(0, 180)
            slider.setValue(get_alpha())
            slider.setFixedWidth(100)
            val_lbl = QLabel(str(get_alpha()))
            val_lbl.setFixedWidth(28)

            def _alpha_changed(v):  #vers 1
                set_alpha(v)
                val_lbl.setText(str(v))
                if pw: pw.update()
            slider.valueChanged.connect(_alpha_changed)

            row.addWidget(lbl)
            row.addWidget(swatch)
            row.addWidget(pick_btn)
            row.addWidget(alpha_lbl)
            row.addWidget(slider)
            row.addWidget(val_lbl)
            parent_layout.addLayout(row)

        # --- Sphere colour ---
        grp_sph = QGroupBox("Spheres")
        sph_lay = QVBoxLayout(grp_sph)
        _colour_row(
            sph_lay, "Sphere",
            lambda: tuple(getattr(pw or self, '_sphere_color', (80, 200, 220))),
            lambda c: setattr(pw or self, '_sphere_color', c),
            lambda:   getattr(pw or self, '_sphere_alpha', 25),
            lambda v: setattr(pw or self, '_sphere_alpha', v))
        root.addWidget(grp_sph)

        # --- Box colour ---
        grp_box = QGroupBox("Boxes")
        box_lay = QVBoxLayout(grp_box)
        _colour_row(
            box_lay, "Box",
            lambda: tuple(getattr(pw or self, '_box_color', (220, 180, 50))),
            lambda c: setattr(pw or self, '_box_color', c),
            lambda:   getattr(pw or self, '_box_alpha', 30),
            lambda v: setattr(pw or self, '_box_alpha', v))
        root.addWidget(grp_box)

        # --- Reset + Close ---
        btn_row = QHBoxLayout()
        reset_btn = QPushButton("Reset Defaults")
        def _reset():  #vers 1
            tgt = pw or self
            tgt._sphere_color = (80, 200, 220)
            tgt._sphere_alpha = 25
            tgt._box_color    = (220, 180, 50)
            tgt._box_alpha    = 30
            if pw: pw.update()
            dlg.accept()
            self._show_shaders_dialog()
        reset_btn.clicked.connect(_reset)
        close_btn = QPushButton("Close")
        close_btn.clicked.connect(dlg.accept)
        btn_row.addWidget(reset_btn)
        btn_row.addStretch()
        btn_row.addWidget(close_btn)
        root.addLayout(btn_row)

        dlg.exec()


# - Marker 7


#------ Col functions


    def _toggle_col_view(self): #vers 1
        """Toggle between detail table and compact thumbnail+name list."""
        if self._col_view_mode == 'list':
            self._col_view_mode = 'detail'
            self.collision_list.setVisible(False)
            self.col_compact_list.setVisible(True)
            self.col_view_toggle_btn.setText("[=]")
            self.col_view_toggle_btn.setToolTip("Switch to detail table view")
            if (self.col_compact_list.rowCount() == 0
                    and self.collision_list.rowCount() > 0
                    and self.current_col_file):
                self._populate_compact_col_list()
        else:
            self._col_view_mode = 'list'
            self.col_compact_list.setVisible(False)
            self.collision_list.setVisible(True)
            self.col_view_toggle_btn.setText("[T]")
            self.col_view_toggle_btn.setToolTip("Switch to compact thumbnail view")

    def _populate_compact_col_list(self): #vers 1
        """Fill compact two-column list (icon + name/version/counts)."""
        try:
            self.col_compact_list.setRowCount(0)
            models = getattr(self.current_col_file, 'models', [])
            for i, model in enumerate(models):
                self.col_compact_list.insertRow(i)

                # Col 0: real collision thumbnail
                icon_item = QTableWidgetItem()
                pm = self._generate_collision_thumbnail(model, 64, 64,
                                yaw=self._thumb_yaw, pitch=self._thumb_pitch)
                icon_item.setData(Qt.ItemDataRole.DecorationRole, pm)
                self.col_compact_list.setItem(i, 0, icon_item)

                # Col 1: name + stats
                name = getattr(model, 'name', '') or f'model_{i}'
                ver  = getattr(model, 'version', None)
                ver_str = ver.name if hasattr(ver, 'name') else str(ver) if ver else '?'
                spheres = len(getattr(model, 'spheres',  []))
                boxes   = len(getattr(model, 'boxes',    []))
                verts   = len(getattr(model, 'vertices', []))
                faces   = len(getattr(model, 'faces',    []))

                line1 = name
                line2 = "Version: " + ver_str
                line3 = "Spheres: " + str(spheres) + "  Boxes: " + str(boxes)
                line4 = "Verts: "   + str(verts)   + "  Faces: " + str(faces)
                details = line1 + "\n" + line2 + "\n" + line3 + "\n" + line4

                det_item = QTableWidgetItem(details)
                det_item.setToolTip(details)
                self.col_compact_list.setItem(i, 1, det_item)
                self.col_compact_list.setRowHeight(i, 72)

            self.col_compact_list.setColumnWidth(0, 72)
            # Update middle panel header with model count
            hdr = getattr(self, '_col_models_header', None)
            if hdr:
                n = self.col_compact_list.rowCount()
                hdr.setText(f"COL Models  ({n})" if n else "COL Models")
        except Exception as e:
            print("_populate_compact_col_list error: " + str(e))

    def _on_compact_col_selected(self): #vers 3
        """Handle compact [=] list selection."""
        try:
            rows = self.col_compact_list.selectionModel().selectedRows()
            if rows:
                self._select_model_by_row(rows[0].row())
        except Exception as e:
            print("_on_compact_col_selected error: " + str(e))


    #    Selection helpers                                                  


    #    Sort                                                               


    #    Pin / lock entries from editing                                    


    #    IDE-linked operations                                              


    def dragEnterEvent(self, event): #vers 1
        """Accept .col and .img files."""
        if self._dropped_files(event):
            event.acceptProposedAction()
        else:
            event.ignore()

    def dragMoveEvent(self, event): #vers 1
        """Keep accepting while over the workshop."""
        self.dragEnterEvent(event)

    def dropEvent(self, event): #vers 2
        """Drop .col/.img: empty workshop opens it; loaded one asks add/new tab."""
        paths = self._dropped_files(event)
        if not paths:
            event.ignore()
            return
        event.acceptProposedAction()
        loaded = bool(getattr(self.current_col_file, 'models', None))
        tw = getattr(self.main_window, 'main_tab_widget', None)
        if loaded:
            from PyQt6.QtWidgets import QMessageBox
            cols = [p for p in paths if p.lower().endswith('.col')]
            names = ", ".join(os.path.basename(p) for p in paths[:3]) + (" ..." if len(paths) > 3 else "")
            box = QMessageBox(self)
            box.setWindowTitle("Dropped COL")
            box.setText(f"{names}\n\nAdd to the open file, or open in a new tab?")
            add_btn = box.addButton("Add to current", QMessageBox.ButtonRole.AcceptRole) if cols else None
            new_btn = box.addButton("Open in new tab", QMessageBox.ButtonRole.ActionRole) if tw is not None else None
            box.addButton(QMessageBox.StandardButton.Cancel)
            box.exec()
            clicked = box.clickedButton()
            if add_btn is not None and clicked is add_btn:
                self._add_models_from_files(cols)
                for path in paths:
                    if path.lower().endswith('.img') and tw is not None:
                        open_col_workshop(self.main_window, path)
            elif new_btn is not None and clicked is new_btn:
                for path in paths:
                    open_col_workshop(self.main_window, path)
            return
        first, rest = paths[0], paths[1:]
        if first.lower().endswith('.img'):
            self.load_from_img_archive(first)
        else:
            self.open_col_file(first)
        if tw is not None and tw.indexOf(self.parentWidget()) >= 0:
            tw.setTabText(tw.indexOf(self.parentWidget()), os.path.splitext(os.path.basename(first))[0])
        if rest and tw is not None:
            for path in rest:
                open_col_workshop(self.main_window, path)


    def _find_all_paint_btns(self): #vers 1
        """Return all paint buttons from both icon and text panels."""
        btns = []
        b = getattr(self, 'paint_btn', None)
        if b: btns.append(b)
        # Walk icon panel for any other paint_btn that was overwritten
        ip = getattr(self, '_transform_icon_panel_ref', None)
        if ip:
            from PyQt6.QtWidgets import QPushButton
            for child in ip.findChildren(QPushButton):
                if child.toolTip() and 'paint' in child.toolTip().lower()                    and child not in btns:
                    btns.append(child)
        return btns

    def _set_col_buttons_enabled(self, enabled: bool): #vers 1
        """Enable/disable all transform buttons in BOTH icon and text panels.
        The text panel overwrites self.X refs, so when the icon panel is visible
        (narrow mode) those refs point to hidden buttons. Walk the icon panel too.
        """
        col_btn_attrs = [
            'flip_vert_btn', 'flip_horz_btn', 'rotate_cw_btn', 'rotate_ccw_btn',
            'analyze_btn', 'copy_btn', 'delete_surface_btn', 'duplicate_surface_btn',
            'paint_btn', 'surface_type_btn', 'surface_edit_btn', 'build_from_txd_btn',
            'show_shadow_btn', 'create_shadow_btn', 'remove_shadow_btn',
            'compress_btn', 'uncompress_btn', 'switch_btn', 'convert_btn',
        ]
        for attr in col_btn_attrs:
            btn = getattr(self, attr, None)
            if btn is not None:
                btn.setEnabled(enabled)
        icon_panel = getattr(self, '_transform_icon_panel_ref', None)
        if icon_panel:
            from PyQt6.QtWidgets import QPushButton
            for btn in icon_panel.findChildren(QPushButton):
                btn.setEnabled(enabled)


    def showEvent(self, event): #vers 1
        """When COL workshop becomes visible, try to populate from loaded IMG."""
        super().showEvent(event)
        if (not self.standalone_mode and
                hasattr(self, 'col_list_widget') and
                self.col_list_widget is not None and
                self.col_list_widget.count() == 0):
            # Try to get current IMG from main window
            if self.main_window and hasattr(self.main_window, 'current_img'):
                img = self.main_window.current_img
                if img and img != getattr(self, 'current_img', None):
                    self.current_img = img
                    self._load_img_col_list()

    def _on_col_selected(self, item): #vers 2
        """Handle COL file selection from left panel list."""
        try:
            entry = item.data(Qt.ItemDataRole.UserRole)
            if entry and self.current_img:
                self._open_col_from_img_entry(self.current_img, entry)
        except Exception as e:
            err = str(e)
            if self.main_window and hasattr(self.main_window, 'log_message'):
                self.main_window.log_message(f"Error selecting COL: {err}")
            else:
                QMessageBox.critical(self, "Error selecting COL", err)


    def _show_col_search(self): #vers 1
        """Toggle COL search box visibility."""
        if hasattr(self, 'col_search_box'):
            visible = not self.col_search_box.isVisible()
            self.col_search_box.setVisible(visible)
            if visible:
                self.col_search_box.setFocus()
            else:
                self.col_search_box.clear()


    def _filter_col_list(self, text: str): #vers 1
        """Filter COL list by search text."""
        if not hasattr(self, 'col_list_widget'): return
        for i in range(self.col_list_widget.count()):
            item = self.col_list_widget.item(i)
            item.setHidden(bool(text) and text.lower() not in item.text().lower())


    def _project_model_2d(self, model, width, height, padding=8,
                          yaw=0.0, pitch=0.0,
                          flip_h=False, flip_v=False): #vers 3
        """Project COL model geometry to 2D canvas using yaw/pitch rotation."""
        import math
        def _rot(pts3):  #vers 1
            result = []
            yr = math.radians(yaw)
            pr = math.radians(pitch)
            cy, sy = math.cos(yr), math.sin(yr)
            cp, sp = math.cos(pr), math.sin(pr)
            for x, y, z in pts3:
                # yaw around Z axis
                rx = x*cy - y*sy
                ry = x*sy + y*cy
                rz = z
                # pitch around X axis
                rx2 = rx
                ry2 = ry*cp - rz*sp
                rz2 = ry*sp + rz*cp
                result.append((rx2, ry2))  # project onto screen plane
            return result

        def _pts3(model):  #vers 1
            def vc(v):  #vers 1
                if hasattr(v,'position'): return (v.position.x,v.position.y,v.position.z)
                return (v.x,v.y,v.z)
            def sc(s):  #vers 1
                c = s.center
                if hasattr(c,'x'): return (c.x,c.y,c.z)
                return (c[0],c[1],c[2])
            def bc(b, mn):  #vers 1
                pt = (b.min_point if mn else b.max_point) if hasattr(b,'min_point') else (b.min if mn else b.max)
                if hasattr(pt,'x'): return (pt.x,pt.y,pt.z)
                return (pt[0],pt[1],pt[2])
            pts = []
            for s in getattr(model,'spheres',[]): x,y,z=sc(s); r=s.radius; pts+=[(x-r,y-r,z-r),(x+r,y+r,z+r)]
            for b in getattr(model,'boxes',  []): pts+=[bc(b,True),bc(b,False)]
            for v in getattr(model,'vertices',[]): pts.append(vc(v))
            return pts

        pts_3d = _pts3(model)
        pts_2d = _rot(pts_3d) if pts_3d else []
        if not pts_2d:
            return 1.0, width//2, height//2, []
        xs = [p[0] for p in pts_2d]
        ys = [p[1] for p in pts_2d]
        mn_x, mx_x = min(xs), max(xs)
        mn_y, mx_y = min(ys), max(ys)
        rng_x = mx_x - mn_x or 1.0
        rng_y = mx_y - mn_y or 1.0
        scale = min((width - padding*2) / rng_x, (height - padding*2) / rng_y)
        cx = (mn_x + mx_x) / 2
        cy = (mn_y + mx_y) / 2
        ox = width  / 2 - cx * scale
        oy = height / 2 - cy * scale

        result = []
        for px, py in pts_2d:
            sx = px * scale + ox
            sy = py * scale + oy
            if flip_h: sx = width - sx
            if flip_v: sy = height - sy
            result.append((sx, sy))
        return scale, ox, oy, result

    def _draw_col_model(self, painter, model, width, height, padding=4,
                       yaw=0.0, pitch=0.0,
                       flip_h=False, flip_v=False): #vers 3
        """Draw COL model onto a QPainter — used by both thumbnail and preview."""
        from PyQt6.QtGui import QPen, QBrush, QColor
        from PyQt6.QtCore import QRectF, QPointF
        import math

        import math
        scale, ox, oy, _ = self._project_model_2d(
            model, width, height, padding,
            yaw=yaw, pitch=pitch, flip_h=flip_h, flip_v=flip_v)

        yr = math.radians(yaw);  cy, sy = math.cos(yr), math.sin(yr)
        pr = math.radians(pitch); cp, sp = math.cos(pr), math.sin(pr)

        def _to2d(x, y, z):  #vers 1
            rx  = x*cy - y*sy
            ry  = x*sy + y*cy
            rx2 = rx
            ry2 = ry*cp - z*sp
            sx = rx2 * scale + ox
            sy2 = ry2 * scale + oy
            if flip_h: sx  = width  - sx
            if flip_v: sy2 = height - sy2
            return sx, sy2

        def _get3(obj):  #vers 1
            if hasattr(obj,'x'):        return obj.x, obj.y, obj.z
            elif hasattr(obj,'position'): return obj.position.x, obj.position.y, obj.position.z
            else: return float(obj[0]), float(obj[1]), float(obj[2])

        def proj_pt(obj):  #vers 1
            return _to2d(*_get3(obj))

        def wx(v): return (width  - (v*scale+ox)) if flip_h else (v*scale+ox)  #vers 1
        def wy(v): return (height - (v*scale+oy)) if flip_v else (v*scale+oy)  #vers 1

        # Mesh faces — filled triangles (grey)
        verts = getattr(model, 'vertices', [])
        faces = getattr(model, 'faces', [])
        if verts and faces:
            painter.setPen(QPen(QColor(120, 180, 120, 180), 0.5))
            painter.setBrush(QBrush(QColor(60, 120, 60, 80)))
            from PyQt6.QtGui import QPolygonF
            for face in faces:
                idx = getattr(face, 'vertex_indices', None)
                if idx is None:
                    fa = getattr(face, 'a', None)
                    if fa is not None:
                        idx = (fa, face.b, face.c)
                if idx and len(idx) == 3:
                    try:
                        p0x, p0y = proj_pt(verts[idx[0]])
                        p1x, p1y = proj_pt(verts[idx[1]])
                        p2x, p2y = proj_pt(verts[idx[2]])
                        poly = QPolygonF([
                            QPointF(p0x, p0y),
                            QPointF(p1x, p1y),
                            QPointF(p2x, p2y),
                        ])
                        painter.drawPolygon(poly)
                    except (IndexError, AttributeError):
                        pass

        # Boxes — yellow outline
        painter.setPen(QPen(QColor(220, 180, 50), max(1.0, scale * 0.05)))
        painter.setBrush(QBrush(QColor(220, 180, 50, 40)))
        for box in getattr(model, 'boxes', []):
            bmin_obj = box.min_point if hasattr(box, 'min_point') else box.min
            bmax_obj = box.max_point if hasattr(box, 'max_point') else box.max
            x1, y1 = proj_pt(bmin_obj)
            x2, y2 = proj_pt(bmax_obj)
            painter.drawRect(QRectF(min(x1,x2), min(y1,y2),
                                    abs(x2-x1) or 2, abs(y2-y1) or 2))

        # Spheres — cyan outline
        painter.setPen(QPen(QColor(80, 200, 220), max(1.0, scale * 0.05)))
        painter.setBrush(QBrush(QColor(80, 200, 220, 40)))
        for sph in getattr(model, 'spheres', []):
            r = sph.radius * scale
            cx, cy = proj_pt(sph.center)
            painter.drawEllipse(QRectF(cx - r, cy - r, r * 2 or 2, r * 2 or 2))

    def _generate_collision_thumbnail(self, model, width=64, height=64,
                                      yaw=0.0, pitch=0.0): #vers 2
        """Generate a small QPixmap thumbnail of a COL model."""
        from PyQt6.QtGui import QPixmap, QPainter, QColor, QPen
        pixmap = QPixmap(width, height)
        pixmap.fill(self._get_ui_color('viewport_bg'))
        has_data = (getattr(model, 'spheres', []) or
                    getattr(model, 'boxes', []) or
                    getattr(model, 'vertices', []))
        if not has_data:
            painter = QPainter(pixmap)
            painter.setPen(QPen(self._get_ui_color('viewport_text'), 1))
            painter.drawLine(4, 4, width-4, height-4)
            painter.drawLine(width-4, 4, 4, height-4)
            painter.end()
            return pixmap
        painter = QPainter(pixmap)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        self._draw_col_model(painter, model, width, height, padding=4,
                             yaw=yaw, pitch=pitch)
        painter.end()
        return pixmap

    def _render_collision_preview(self, model, width=400, height=400,
                                  yaw=0.0, pitch=0.0,
                                  flip_h=False, flip_v=False): #vers 3
        """Render a full-size QPixmap preview of a COL model.
        yaw/pitch are Euler angles in degrees for free rotation.
        """
        from PyQt6.QtGui import QPixmap, QPainter, QColor, QFont
        from PyQt6.QtCore import Qt
        pixmap = QPixmap(width, height)
        pixmap.fill(self._get_ui_color('viewport_bg'))
        painter = QPainter(pixmap)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        has_data = (getattr(model, 'spheres', []) or
                    getattr(model, 'boxes', []) or
                    getattr(model, 'vertices', []))

        if not has_data:
            painter.setPen(self._get_ui_color('viewport_text'))
            painter.setFont(QFont('Arial', 11))
            painter.drawText(pixmap.rect(), Qt.AlignmentFlag.AlignCenter, "No geometry data")
            painter.end()
            return pixmap

        self._draw_col_model(painter, model, width, height, padding=20,
                            yaw=yaw, pitch=pitch,
                            flip_h=flip_h, flip_v=flip_v)

        # Legend
        painter.setFont(QFont('Arial', 8))
        y = height - 52
        for color, label in [
            (QColor(60, 120, 60),   f"Mesh  F:{len(getattr(model,'faces',[]))} V:{len(getattr(model,'vertices',[]))}"),
            (QColor(220, 180, 50),  f"Boxes  {len(getattr(model,'boxes',[]))}"),
            (QColor(80, 200, 220),  f"Spheres  {len(getattr(model,'spheres',[]))}"),
        ]:
            painter.setPen(color)
            painter.drawText(6, y, label)
            y += 14

        # Model name
        name = getattr(model, 'name', '')
        if name:
            painter.setPen(self._get_ui_color('border'))
            painter.setFont(QFont('Arial', 9))
            painter.drawText(6, 14, name)

        painter.end()
        return pixmap

    def _on_collision_selected(self): #vers 8
        """Handle [T] detail table selection."""
        try:
            rows = self.collision_list.selectionModel().selectedRows()
            if rows:
                self._select_model_by_row(rows[0].row())
        except Exception as e:
            print("_on_collision_selected error: " + str(e))

    def _select_model_by_row(self, row): #vers 3
        """Load model by row index into preview — works for both list views."""
        try:
            if not self.current_col_file:
                return
            models = getattr(self.current_col_file, 'models', [])
            if row < 0 or row >= len(models):
                return
            model = models[row]
            model_name = getattr(model, 'name', f'Model_{row}')

            # Debug counts
            nb = len(getattr(model,'boxes',[]));  ns = len(getattr(model,'spheres',[]))
            nv = len(getattr(model,'vertices',[])); nf = len(getattr(model,'faces',[]))
            print(f"SELECT [{row}] {model_name}: V={nv} F={nf} B={nb} S={ns}")

            # Name field
            if hasattr(self, 'info_name'):
                self.info_name.setText(model_name)

            # Push model into 2D viewport
            pw = getattr(self, 'preview_widget', None)
            if pw:
                if VIEWPORT_AVAILABLE and isinstance(pw, COL3DViewport):
                    pw.set_current_model(model, row)
                else:
                    w = max(400, pw.width()); h = max(400, pw.height())
                    pw.setPixmap(self._render_collision_preview(model, w, h))
                    pw.setScaledContents(False)
            # Also update GL viewport if in GL mode (COL meshes as DFF-like geometry)
            if getattr(self, '_gl_mode', False):
                try:
                    from apps.methods.col_operations import col_to_dff_geometry
                    g, mats = col_to_dff_geometry(model)
                    if g: self.load_dff_in_gl(g, mats)
                except Exception: pass

            # Spin thumbnail in detail list
            self._start_thumbnail_spin(row, model)

        except Exception as e:
            import traceback; traceback.print_exc()
            print(f"_select_model_by_row error: {e}")


    def _show_model_details(self, model, index): #vers 1
        """Show detailed model information dialog"""
        from PyQt6.QtWidgets import QDialog, QTextEdit, QVBoxLayout, QPushButton

        dialog = QDialog(self)
        dialog.setWindowTitle(f"Model Details - {model.name}")
        dialog.setMinimumSize(500, 400)

        layout = QVBoxLayout(dialog)

        # Create detailed info text
        info_text = f"""Model: {model.name}
    Index: {index}
    Version: {model.version.name if hasattr(model.version, 'name') else model.version}

    Bounding Box:
    Center: ({model.bounding_box.center.x:.3f}, {model.bounding_box.center.y:.3f}, {model.bounding_box.center.z:.3f})
    Min: ({model.bounding_box.min.x:.3f}, {model.bounding_box.min.y:.3f}, {model.bounding_box.min.z:.3f})
    Max: ({model.bounding_box.max.x:.3f}, {model.bounding_box.max.y:.3f}, {model.bounding_box.max.z:.3f})
    Radius: {model.bounding_box.radius:.3f}

    Collision Data:
    Spheres: {len(model.spheres)}
    Boxes: {len(model.boxes)}
    Vertices: {len(model.vertices)}
    Faces: {len(model.faces)}

    """

        # Add first 3 vertices if available
        if len(model.vertices) > 0:
            info_text += "\nVertices:\n"
            for i in range(min(30000, len(model.vertices))):
                v = model.vertices[i]
                if hasattr(v, 'position'):
                    info_text += f"  [{i}] ({v.position.x:.3f}, {v.position.y:.3f}, {v.position.z:.3f})\n"
                else:
                    info_text += f"  [{i}] ({v.x:.3f}, {v.y:.3f}, {v.z:.3f})\n"

        # Add material info from faces
        if len(model.faces) > 0:
            materials = set()
            for face in model.faces:
                if hasattr(face, 'material'):
                    mat_id = face.material.material_id if hasattr(face.material, 'material_id') else face.material
                    materials.add(mat_id)
            info_text += f"\nUnique Materials: {len(materials)}\n"
            info_text += f"Material IDs: {sorted(materials)}\n"

        text_edit = QTextEdit()
        text_edit.setPlainText(info_text)
        text_edit.setReadOnly(True)
        layout.addWidget(text_edit)

        # Copy button
        copy_btn = QPushButton("Copy to Clipboard")
        copy_btn.clicked.connect(lambda: self._copy_text_to_clipboard(info_text))
        layout.addWidget(copy_btn)

        # Close button
        close_btn = QPushButton("Close")
        close_btn.clicked.connect(dialog.accept)
        layout.addWidget(close_btn)

        dialog.exec()


    def _copy_model_info(self, model, index): #vers 1
        """Copy model info to clipboard"""
        info = f"{model.name} | S:{len(model.spheres)} B:{len(model.boxes)} V:{len(model.vertices)} F:{len(model.faces)}"
        self._copy_text_to_clipboard(info)
        if hasattr(self, 'status_bar'):
            self.status_bar.showMessage("Model info copied to clipboard", 2000)


    def _copy_text_to_clipboard(self, text): #vers 1
        """Copy text to system clipboard"""
        from PyQt6.QtWidgets import QApplication
        clipboard = QApplication.clipboard()
        clipboard.setText(text)


    def _populate_collision_list(self): #vers 7
        """Populate [T] detail table — 8 columns, icon badges on counts > 0."""
        try:
            self.collision_list.setRowCount(0)
            if not self.current_col_file or not hasattr(self.current_col_file, 'models'):
                return

            # Build icon pixmaps once (16px, themed colour)
            icon_color = self._get_icon_color()
            from apps.methods.imgfactory_svg_icons import SVGIconFactory as _SVG
            from PyQt6.QtGui import QPixmap

            def _px(icon_fn, color=None):  #vers 1
                """Get 14px QPixmap from an SVG icon factory method."""
                try:
                    ico = icon_fn(size=14, color=color or icon_color)
                    return ico.pixmap(14, 14)
                except Exception:
                    return QPixmap()

            sphere_px = _px(_SVG.sphere_icon, '#50c8e0')   # cyan
            box_px    = _px(_SVG.box_icon,    '#dcb432')   # yellow
            face_px   = _px(_SVG.mesh_icon,   '#6496dc')   # blue
            # No dedicated vert icon — draw a tiny dot pixmap inline
            vert_px   = QPixmap(14, 14)
            from PyQt6.QtGui import QPainter, QColor, QBrush
            from PyQt6.QtCore import QRectF
            vert_px.fill(QColor(0, 0, 0, 0))
            vp = QPainter(vert_px)
            vp.setRenderHint(QPainter.RenderHint.Antialiasing)
            vp.setBrush(QBrush(QColor(100, 200, 120)))
            vp.setPen(QColor(100, 200, 120))
            for ox, oy in [(2,2),(8,2),(5,9)]:
                vp.drawEllipse(QRectF(ox, oy, 4, 4))
            vp.end()

            icon_map = {4: sphere_px, 5: box_px, 6: vert_px, 7: face_px}

            models = self.current_col_file.models
            self.collision_list.setUpdatesEnabled(False)

            for i, model in enumerate(models):
                name     = getattr(model, 'name', '') or f'model_{i}'
                version  = getattr(model, 'version', None)
                ver_str  = version.name if hasattr(version,'name') else str(version) if version else '?'
                ver_short = ver_str.replace('COL_','COL').replace('COLVersion.','')
                # Type = fourcc string, Version = game target label
                header   = getattr(model, 'header', None)
                fourcc   = getattr(header, 'fourcc', b'') if header else b''
                try:    type_str = fourcc.decode('ascii').rstrip('\x00')
                except Exception: type_str = str(fourcc)
                ver_label = {'COL1':'GTA III/VC','COL2':'SA PS2',
                             'COL3':'SA PC/Xbox','COL4':'SA (unused)'
                             }.get(ver_short, ver_short)
                spheres  = len(getattr(model, 'spheres',  []))
                boxes    = len(getattr(model, 'boxes',    []))
                vertices = len(getattr(model, 'vertices', []))
                faces    = len(getattr(model, 'faces',    []))
                bounds   = getattr(model, 'bounds', None)
                radius   = getattr(bounds, 'radius', 0.0) if bounds else 0.0

                row = self.collision_list.rowCount()
                self.collision_list.insertRow(row)

                def _item(text, col=None, idx=None):  #vers 1
                    it = QTableWidgetItem(str(text))
                    it.setFlags(it.flags() & ~Qt.ItemFlag.ItemIsEditable)
                    it.setTextAlignment(Qt.AlignmentFlag.AlignCenter |
                                        Qt.AlignmentFlag.AlignVCenter)
                    if idx is not None:
                        it.setData(Qt.ItemDataRole.UserRole, idx)
                    # Add icon if count > 0 and we have a pixmap for this col
                    if col in icon_map and isinstance(text, int) and text > 0:
                        it.setIcon(QIcon(icon_map[col]))
                    return it

                from PyQt6.QtGui import QIcon

                name_it = QTableWidgetItem(name)
                name_it.setFlags(name_it.flags() & ~Qt.ItemFlag.ItemIsEditable)
                name_it.setTextAlignment(Qt.AlignmentFlag.AlignLeft |
                                         Qt.AlignmentFlag.AlignVCenter)
                name_it.setData(Qt.ItemDataRole.UserRole, i)

                self.collision_list.setItem(row, 0, name_it)
                self.collision_list.setItem(row, 1, _item(type_str))
                self.collision_list.setItem(row, 2, _item(ver_label))
                self.collision_list.setItem(row, 3, _item(f"{radius:.2f}"))
                self.collision_list.setItem(row, 4, _item(spheres,  col=4))
                self.collision_list.setItem(row, 5, _item(boxes,    col=5))
                self.collision_list.setItem(row, 6, _item(vertices, col=6))
                self.collision_list.setItem(row, 7, _item(faces,    col=7))
                self.collision_list.setRowHeight(row, 22)

            # Column widths
            self.collision_list.setIconSize(QSize(14, 14))
            hdr = self.collision_list.horizontalHeader()
            hdr.resizeSection(0, 160)
            for c in range(1, 8):
                hdr.resizeSection(c, 68)
            hdr.setStretchLastSection(True)

            self.collision_list.setUpdatesEnabled(True)
            self.collision_list.viewport().update()

        except Exception as e:
            import traceback; traceback.print_exc()
            print(f"Error populating collision table: {str(e)}")


# ----- Render functions


    def _show_settings_hotkeys(self): #vers 1
        """Show settings dialog with hotkey customization"""
        from PyQt6.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout, QTabWidget,
                                    QWidget, QLabel, QLineEdit, QPushButton,
                                    QGroupBox, QFormLayout, QKeySequenceEdit)
        from PyQt6.QtCore import Qt

        dialog = QDialog(self)
        dialog.setWindowTitle(App_name + " Settings")
        dialog.setMinimumWidth(600)
        dialog.setMinimumHeight(500)

        layout = QVBoxLayout(dialog)

        # Create tabs
        tabs = QTabWidget()

        # === HOTKEYS TAB ===
        hotkeys_tab = QWidget()
        hotkeys_layout = QVBoxLayout(hotkeys_tab)

        # File Operations Group
        file_group = QGroupBox("File Operations")
        file_form = QFormLayout()

        self.hotkey_edit_open = QKeySequenceEdit(self.hotkey_open.key())
        file_form.addRow("Open col:", self.hotkey_edit_open)

        self.hotkey_edit_save = QKeySequenceEdit(self.hotkey_save.key())
        file_form.addRow("Save col:", self.hotkey_edit_save)

        self.hotkey_edit_force_save = QKeySequenceEdit(self.hotkey_force_save.key())
        force_save_layout = QHBoxLayout()
        force_save_layout.addWidget(self.hotkey_edit_force_save)
        force_save_hint = QLabel("(Force save even if unmodified)")
        force_save_hint.setStyleSheet("color: #888; font-style: italic;")
        force_save_layout.addWidget(force_save_hint)
        file_form.addRow("Force Save:", force_save_layout)

        self.hotkey_edit_save_as = QKeySequenceEdit(self.hotkey_save_as.key())
        file_form.addRow("Save As:", self.hotkey_edit_save_as)

        self.hotkey_edit_close = QKeySequenceEdit(self.hotkey_close.key())
        file_form.addRow("Close:", self.hotkey_edit_close)

        file_group.setLayout(file_form)
        hotkeys_layout.addWidget(file_group)

        # Edit Operations Group
        edit_group = QGroupBox("Edit Operations")
        edit_form = QFormLayout()

        self.hotkey_edit_undo = QKeySequenceEdit(self.hotkey_undo.key())
        edit_form.addRow("Undo:", self.hotkey_edit_undo)

        self.hotkey_edit_copy = QKeySequenceEdit(self.hotkey_copy.key())
        edit_form.addRow("Copy Collision:", self.hotkey_edit_copy)

        self.hotkey_edit_paste = QKeySequenceEdit(self.hotkey_paste.key())
        edit_form.addRow("Paste Collision:", self.hotkey_edit_paste)

        self.hotkey_edit_delete = QKeySequenceEdit(self.hotkey_delete.key())
        edit_form.addRow("Delete:", self.hotkey_edit_delete)

        self.hotkey_edit_duplicate = QKeySequenceEdit(self.hotkey_duplicate.key())
        edit_form.addRow("Duplicate:", self.hotkey_edit_duplicate)

        self.hotkey_edit_rename = QKeySequenceEdit(self.hotkey_rename.key())
        edit_form.addRow("Rename:", self.hotkey_edit_rename)

        edit_group.setLayout(edit_form)
        hotkeys_layout.addWidget(edit_group)

        # Collision Group
        coll_group = QGroupBox("Collision Operations")
        coll_form = QFormLayout()

        self.hotkey_edit_import = QKeySequenceEdit(self.hotkey_import.key())
        coll_form.addRow("Import Collision:", self.hotkey_edit_import)

        self.hotkey_edit_export = QKeySequenceEdit(self.hotkey_export.key())
        coll_form.addRow("Export Collision:", self.hotkey_edit_export)

        self.hotkey_edit_export_all = QKeySequenceEdit(self.hotkey_export_all.key())
        coll_form.addRow("Export All:", self.hotkey_edit_export_all)

        coll_group.setLayout(coll_form)
        hotkeys_layout.addWidget(coll_group)

        # View Operations Group
        view_group = QGroupBox("View Operations")
        view_form = QFormLayout()

        self.hotkey_edit_refresh = QKeySequenceEdit(self.hotkey_refresh.key())
        view_form.addRow("Refresh:", self.hotkey_edit_refresh)

        self.hotkey_edit_properties = QKeySequenceEdit(self.hotkey_properties.key())
        view_form.addRow("Properties:", self.hotkey_edit_properties)

        self.hotkey_edit_find = QKeySequenceEdit(self.hotkey_find.key())
        view_form.addRow("Find/Search:", self.hotkey_edit_find)

        self.hotkey_edit_help = QKeySequenceEdit(self.hotkey_help.key())
        view_form.addRow("Help:", self.hotkey_edit_help)

        view_group.setLayout(view_form)
        hotkeys_layout.addWidget(view_group)

        hotkeys_layout.addStretch()

        # Reset to defaults button
        reset_hotkeys_btn = QPushButton("Reset to Plasma6 Defaults")
        reset_hotkeys_btn.clicked.connect(lambda: self._reset_hotkeys_to_defaults(dialog))
        hotkeys_layout.addWidget(reset_hotkeys_btn)

        tabs.addTab(hotkeys_tab, "Keyboard Shortcuts")

        # === GENERAL TAB (for future settings) ===
        general_tab = QWidget()
        general_layout = QVBoxLayout(general_tab)

        placeholder_label = QLabel("Additional settings will appear here in future versions.")
        placeholder_label.setStyleSheet("color: #888; font-style: italic; padding: 20px;")
        placeholder_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        general_layout.addWidget(placeholder_label)
        general_layout.addStretch()

        tabs.addTab(general_tab, "General")

        layout.addWidget(tabs)

        # Dialog buttons
        button_layout = QHBoxLayout()
        button_layout.addStretch()

        cancel_btn = QPushButton("Cancel")
        cancel_btn.clicked.connect(dialog.reject)
        button_layout.addWidget(cancel_btn)

        apply_btn = QPushButton("Apply")
        apply_btn.clicked.connect(lambda: self._apply_hotkey_settings(dialog))
        button_layout.addWidget(apply_btn)

        ok_btn = QPushButton("OK")
        ok_btn.setDefault(True)
        ok_btn.clicked.connect(lambda: self._apply_hotkey_settings(dialog, close=True))
        button_layout.addWidget(ok_btn)

        layout.addLayout(button_layout)

        dialog.exec()

    def _show_col_info(self): #vers 4
        """Show TXD Workshop information dialog - About and capabilities"""
        dialog = QDialog(self)
        dialog.setWindowTitle("About COL Workshop")
        dialog.setMinimumWidth(600)
        dialog.setMinimumHeight(500)

        layout = QVBoxLayout(dialog)
        layout.setSpacing(15)

        # Header
        header = QLabel(f"COL Workshop - {App_name}")
        header.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        header.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(header)

        # Author info
        author_label = QLabel("Author: X-Seti")
        author_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(author_label)

        # Version info
        version_label = QLabel("Version: 1.5 - October 2025")
        version_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(version_label)

        layout.addWidget(QLabel(""))  # Spacer

        # Capabilities section
        capabilities = QTextEdit()
        capabilities.setReadOnly(True)
        capabilities.setMaximumHeight(350)

        info_text = """<b>COL Workshop Capabilities:</b><br><br>

<b>✓ File Operations:</b><br>


<b>✓ Collision Viewing & Editing:</b><br>


<b>✓ Collision Management:</b><br>


<b>✓ Collision Surface Painting:</b><br>


<b>✓ Format Support:</b><br>


<b>✓ Advanced Features:</b><br>"""

        # Add format support dynamically
        formats_available = []

        # Standard formats (always via PIL)

        info_text += "<br>".join(formats_available)
        info_text += "<br><br>"

        # Settings info
        info_text += """<b>✓ Customization:</b><br>
- Adjustable texture name length (8-64 chars)<br>
- Button display modes (Icons/Text/Both)<br>
- Font customization<br>
- Preview zoom and pan offsets<br><br>

<b>Keyboard Shortcuts:</b><br>
- Ctrl+O: Open COL<br>
- Ctrl+S: Save COL<br>
- Ctrl+I: Import Collision col, cst, 3ds<br>
- Ctrl+E: Export Selected col, cst, 3ds<br>
- Ctrl+Z: Undo<br>
- Delete: Remove Collision<br>
- Ctrl+D: Duplicate Collision<br>"""

        capabilities.setHtml(info_text)
        layout.addWidget(capabilities)

        # Close button
        close_btn = QPushButton("Close")
        close_btn.clicked.connect(dialog.accept)
        close_btn.setDefault(True)
        layout.addWidget(close_btn)

        dialog.exec()


#class SvgIcons: #vers 1 - Once functions are updated this class will be moved to the bottom
    """SVG icon data to QIcon with theme color support"""

#moved to scg_icon_factory


# --- External AI upscaler integration helper ---
import sys


# Compatibility alias for imports

def open_col_workshop(main_window, img_path=None): #vers 3
    """Open COL Workshop - embedded in tab if main_window has tab widget, standalone otherwise"""
    try:
        from PyQt6.QtWidgets import QVBoxLayout, QWidget

        # Standalone mode
        if not main_window or not hasattr(main_window, 'main_tab_widget'):
            workshop = COLWorkshop(None, main_window)
            workshop.setWindowFlags(Qt.WindowType.Window)
            if img_path:
                ext = img_path.lower()
                if ext.endswith('.col'):
                    if hasattr(workshop, 'open_col_file'):
                        workshop.open_col_file(img_path)
                    elif hasattr(workshop, 'load_col_file'):
                        workshop.load_col_file(img_path)
                elif ext.endswith('.img'):
                    workshop.load_from_img_archive(img_path)
            elif main_window:
                # No explicit file - load from current IMG if available,
                # matching embedded mode's fallback below.
                img = getattr(main_window, 'current_img', None)
                if img:
                    fp = getattr(img, 'file_path', '') or ''
                    if fp and os.path.isfile(fp):
                        workshop.load_from_img_archive(fp)
            workshop.setWindowTitle(f"COL Workshop - {App_name}")
            workshop.resize(1200, 800)
            workshop.show()
            return workshop

        # Embedded mode - add as tab
        tab_container = QWidget()
        tab_layout = QVBoxLayout(tab_container)
        tab_layout.setContentsMargins(0, 0, 0, 0)

        workshop = COLWorkshop(tab_container, main_window)
        workshop.setWindowFlags(Qt.WindowType.Widget)
        tab_layout.addWidget(workshop)

        if img_path:
            ext = img_path.lower()
            if ext.endswith('.col'):
                if hasattr(workshop, 'open_col_file'):
                    workshop.open_col_file(img_path)
                elif hasattr(workshop, 'load_col_file'):
                    workshop.load_col_file(img_path)
            elif ext.endswith('.img'):
                workshop.load_from_img_archive(img_path)
        elif main_window:
            # No explicit file — load from current IMG if available
            img = getattr(main_window, 'current_img', None)
            if img:
                fp = getattr(img, 'file_path', '') or ''
                if fp and os.path.isfile(fp):
                    workshop.load_from_img_archive(fp)

        tab_label = os.path.splitext(os.path.basename(img_path))[0] if img_path else "COL Workshop"
        try:
            from apps.methods.imgfactory_svg_icons import get_col_file_icon
            icon = get_col_file_icon()
            idx = main_window.main_tab_widget.addTab(tab_container, icon, tab_label)
        except Exception:
            idx = main_window.main_tab_widget.addTab(tab_container, tab_label)
        main_window.main_tab_widget.setCurrentIndex(idx)
        if hasattr(main_window, '_ensure_tab_area_visible'):
            main_window._ensure_tab_area_visible()

        workshop.show()
        return workshop

    except Exception as e:
        if main_window and hasattr(main_window, 'log_message'):
            main_window.log_message(f"Error opening COL Workshop: {str(e)}")
        return None


if __name__ == "__main__":
    import sys
    import traceback

    print(App_name + " Starting.")

    try:
        app = QApplication(sys.argv)
        print("QApplication created")

        workshop = COLWorkshop()
        print(App_name + " instance created")

        workshop.setWindowTitle(App_name + " - Standalone")
        workshop.resize(1200, 800)
        workshop.show()
        print("Window shown, entering event loop")
        print(f"Window visible: {workshop.isVisible()}")
        print(f"Window geometry: {workshop.geometry()}")

        sys.exit(app.exec())

    except Exception as e:
        print(f"ERROR: {e}")
        traceback.print_exc()
        sys.exit(1)

